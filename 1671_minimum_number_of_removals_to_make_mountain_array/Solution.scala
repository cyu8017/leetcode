// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

object Solution {
  def minimumMountainRemovals(nums: Array[Int]): Int = {
    def lis(a: Array[Int]): Array[Int] = {
      val d = scala.collection.mutable.ArrayBuffer[Int]()
      val out = Array.fill(a.length)(0)
      for (i <- a.indices) {
        val x = a(i)
        var lo = 0
        var hi = d.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (d(mid) < x) lo = mid + 1 else hi = mid
        }
        if (lo == d.length) d += x else d(lo) = x
        out(i) = lo + 1
      }
      out
    }
    val n = nums.length
    val l = lis(nums)
    val r = lis(nums.reverse).reverse
    var best = 0
    for (i <- 0 until n if l(i) > 1 && r(i) > 1) {
      best = math.max(best, l(i) + r(i) - 1)
    }
    n - best
  }
}
