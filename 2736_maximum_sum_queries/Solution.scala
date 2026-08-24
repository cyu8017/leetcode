// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

object Solution {
  def maximumSumQueries(nums1: Array[Int], nums2: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums1.length
    val pts = Array.tabulate(n)(i => Array(nums1(i), nums2(i), nums1(i) + nums2(i)))
    java.util.Arrays.sort(pts, (a: Array[Int], b: Array[Int]) => Integer.compare(b(0), a(0)))
    val qs = Array.tabulate(queries.length)(i => Array(queries(i)(0), queries(i)(1), i))
    java.util.Arrays.sort(qs, (a: Array[Int], b: Array[Int]) => Integer.compare(b(0), a(0)))
    val ys = scala.collection.mutable.ArrayBuffer.empty[Int]
    nums2.foreach(ys += _)
    queries.foreach(q => ys += q(1))
    val sorted = ys.sorted
    val uniq = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < sorted.length) {
      if (uniq.isEmpty || uniq.last != sorted(i)) uniq += sorted(i)
      i += 1
    }
    val m = uniq.length
    val bit = Array.fill(m + 2)(-1)
    val ans = Array.ofDim[Int](queries.length)
    var j = 0
    qs.foreach { q =>
      while (j < n && pts(j)(0) >= q(0)) {
        update(bit, m, m - rank(uniq, pts(j)(1)) + 1, pts(j)(2))
        j += 1
      }
      ans(q(2)) = query(bit, m - rank(uniq, q(1)) + 1)
    }
    ans
  }

  private def rank(ys: scala.collection.mutable.ArrayBuffer[Int], y: Int): Int = {
    var lo = 0
    var hi = ys.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ys(mid) < y) lo = mid + 1
      else hi = mid
    }
    lo + 1
  }

  private def update(bit: Array[Int], m: Int, i0: Int, v: Int): Unit = {
    var i = i0
    while (i <= m) {
      bit(i) = math.max(bit(i), v)
      i += i & -i
    }
  }

  private def query(bit: Array[Int], i0: Int): Int = {
    var i = i0
    var best = -1
    while (i > 0) {
      best = math.max(best, bit(i))
      i -= i & -i
    }
    best
  }
}
