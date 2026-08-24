// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

import kotlin.math.abs

class Solution {
    fun findTargetSumWays(nums: IntArray, target: Int): Int {
        val total = nums.sum()
        if ((total + target) % 2 != 0 || abs(target) > total) return 0
        val need = (total + target) / 2
        val dp = IntArray(need + 1)
        dp[0] = 1
        for (num in nums) {
            for (amount in need downTo num) {
                dp[amount] += dp[amount - num]
            }
        }
        return dp[need]
    }
}
