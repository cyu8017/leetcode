// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

object Solution {
  def findTargetSumWays(nums: Array[Int], target: Int): Int = {
    val total = nums.sum
    if ((total + target) % 2 != 0 || math.abs(target) > total) return 0
    val need = (total + target) / 2
    val dp = Array.fill(need + 1)(0)
    dp(0) = 1
    for (num <- nums; amount <- need to num by -1) dp(amount) += dp(amount - num)
    dp(need)
  }
}
