// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

object Solution {
  def longestArithSeqLength(nums: Array[Int]): Int = {
    val dp = Array.fill(nums.length)(scala.collection.mutable.Map.empty[Int, Int])
    var ans = 1
    for (j <- 1 until nums.length; i <- 0 until j) {
      val d = nums(j) - nums(i)
      dp(j)(d) = dp(i).getOrElse(d, 1) + 1
      ans = math.max(ans, dp(j)(d))
    }
    ans
  }
}
