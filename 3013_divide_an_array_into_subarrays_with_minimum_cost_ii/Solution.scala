// LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

object Solution {
  private class BITI(n_ : Int) {
    val n = n_
    val c = Array.ofDim[Int](n_ + 1)
    def upd(x0: Int, d: Int): Unit = {
      var x = x0
      while (x <= n) { c(x) += d; x += x & -x }
    }
    def qry(x0: Int): Int = {
      var x = x0
      var s = 0
      while (x > 0) { s += c(x); x -= x & -x }
      s
    }
  }
  private class BITL(n_ : Int) {
    val n = n_
    val c = Array.ofDim[Long](n_ + 1)
    def upd(x0: Int, d: Long): Unit = {
      var x = x0
      while (x <= n) { c(x) += d; x += x & -x }
    }
    def qry(x0: Int): Long = {
      var x = x0
      var s = 0L
      while (x > 0) { s += c(x); x -= x & -x }
      s
    }
  }

  private def kth(cnt: BITI, m: Int, k0: Int): Int = {
    var k = k0
    var idx = 0
    var bit = 1 << 20
    while (bit != 0) {
      val nidx = idx + bit
      if (nidx <= m && cnt.c(nidx) < k) {
        k -= cnt.c(nidx)
        idx = nidx
      }
      bit >>= 1
    }
    idx + 1
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (a(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }

  private def sumSmallest(cnt: BITI, sum: BITL, uniq: Array[Int], m: Int, kk: Int): Long = {
    if (kk <= 0) return 0
    val r = kth(cnt, m, kk)
    val before = cnt.qry(r - 1)
    var s = sum.qry(r - 1)
    s += (kk - before).toLong * uniq(r - 1)
    s
  }

  def minimumCost(nums: Array[Int], k0: Int, dist: Int): Long = {
    val k = k0 - 1
    val n = nums.length
    val uniq0 = nums.clone()
    scala.util.Sorting.quickSort(uniq0)
    val tmp = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < uniq0.length) {
      if (tmp.isEmpty || uniq0(i) != tmp.last) tmp += uniq0(i)
      i += 1
    }
    val uniq = tmp.toArray
    val m = uniq.length
    val cnt = new BITI(m + 2)
    val sum = new BITL(m + 2)
    i = 1
    while (i <= math.min(dist + 1, n - 1)) {
      val r = lowerBound(uniq, nums(i)) + 1
      cnt.upd(r, 1)
      sum.upd(r, nums(i).toLong)
      i += 1
    }
    val end = math.min(dist + 1, n - 1)
    var kk = math.min(k, end)
    var ans = nums(0).toLong + sumSmallest(cnt, sum, uniq, m, kk)
    i = dist + 2
    while (i < n) {
      val rem = nums(i - dist - 1)
      val r1 = lowerBound(uniq, rem) + 1
      cnt.upd(r1, -1)
      sum.upd(r1, -rem.toLong)
      val add = nums(i)
      val r2 = lowerBound(uniq, add) + 1
      cnt.upd(r2, 1)
      sum.upd(r2, add.toLong)
      kk = math.min(k, dist + 1)
      ans = math.min(ans, nums(0).toLong + sumSmallest(cnt, sum, uniq, m, kk))
      i += 1
    }
    ans
  }
}
