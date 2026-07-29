// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution {
    fun longestArithSeqLength(nums: IntArray): Int {
        val dp = Array(nums.size) { mutableMapOf<Int, Int>() }
        var ans = 1
        for (j in 1 until nums.size) {
            for (i in 0 until j) {
                val d = nums[j] - nums[i]
                val prev = dp[i][d] ?: 1
                val cur = prev + 1
                dp[j][d] = cur
                ans = maxOf(ans, cur)
            }
        }
        return ans
    }
}
