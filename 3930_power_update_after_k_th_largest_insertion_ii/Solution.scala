// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

object Solution {
  def powerUpdate(nums: Array[Int], p: Int, queries: Array[Array[Int]]): Array[Int] = {
    val mod = 1000000007L
    var vals = nums ++ queries.map(_(0))
    vals = vals.sorted
    var uniq = 0
    var i = 0
    while (i < vals.length) {
      if (uniq == 0 || vals(i) != vals(uniq - 1)) {
        vals(uniq) = vals(i)
        uniq += 1
      }
      i += 1
    }
    vals = vals.take(uniq)
    val bit = new Array[Int](vals.length + 1)
    for (x <- nums) add(bit, lowerBound(vals, x) + 1)
    val ans = new Array[Int](queries.length)
    var size = nums.length
    var cur = p.toLong
    i = 0
    while (i < queries.length) {
      add(bit, lowerBound(vals, queries(i)(0)) + 1)
      size += 1
      val x = kth(bit, vals, size - queries(i)(1) + 1)
      cur = powm(cur, x, mod)
      ans(i) = cur.toInt
      i += 1
    }
    ans
  }

  private def add(bit: Array[Int], start: Int): Unit = {
    var i = start
    while (i < bit.length) {
      bit(i) += 1
      i += i & -i
    }
  }

  private def kth(bit: Array[Int], vals: Array[Int], startRank: Int): Int = {
    var idx = 0
    var rank = startRank
    var step = 1
    while ((step << 1) < bit.length) step <<= 1
    while (step > 0) {
      val next = idx + step
      if (next < bit.length && bit(next) < rank) {
        idx = next
        rank -= bit(next)
      }
      step >>= 1
    }
    vals(idx)
  }

  private def lowerBound(vals: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = vals.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (vals(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }

  private def powm(base: Long, exp: Long, mod: Long): Long = {
    var a = base
    var e = exp
    var res = 1L
    while (e > 0) {
      if ((e & 1) != 0) res = res * a % mod
      a = a * a % mod
      e >>= 1
    }
    res
  }
}
