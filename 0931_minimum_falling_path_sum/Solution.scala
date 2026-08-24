// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

object Solution {
  def minFallingPathSum(matrix: Array[Array[Int]]): Int = {
    var dp = matrix(0).clone()
    var r = 1
    while (r < matrix.length) {
      val ndp = Array.ofDim[Int](dp.length)
      var c = 0
      while (c < dp.length) {
        var best = dp(c)
        if (c > 0) best = math.min(best, dp(c - 1))
        if (c + 1 < dp.length) best = math.min(best, dp(c + 1))
        ndp(c) = matrix(r)(c) + best
        c += 1
      }
      dp = ndp
      r += 1
    }
    dp.min
  }
}
