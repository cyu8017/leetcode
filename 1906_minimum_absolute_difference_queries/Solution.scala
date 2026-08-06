// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

object Solution {
  def minDifference(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val pref = Array.ofDim[Int](n + 1, 101)
    for (i <- 0 until n) {
      Array.copy(pref(i), 0, pref(i + 1), 0, 101)
      pref(i + 1)(nums(i)) += 1
    }
    queries.map { q =>
      val left = q(0)
      val right = q(1)
      var prev = -1
      var best = Int.MaxValue
      for (value <- 1 to 100) {
        if (pref(right + 1)(value) - pref(left)(value) > 0) {
          if (prev != -1) best = math.min(best, value - prev)
          prev = value
        }
      }
      if (best == Int.MaxValue) -1 else best
    }
  }
}
