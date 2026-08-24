// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

class Solution {
    fun minimumOperations(nums: MutableList<Int>): Int {
        val n = nums.size
        val INF = 1 shl 30
        val dp = Array(n + 1) { IntArray(4) { INF } }
        dp[0][1] = 0
        dp[0][2] = 0
        dp[0][3] = 0
        for (i in 1..n) {
            val v = nums[i - 1]
            for (g in 1..3) {
                val cost = if (v != g) 1 else 0
                for (prev in 1..g) {
                    dp[i][g] = minOf(dp[i][g], dp[i - 1][prev] + cost)
                }
            }
        }
        return minOf(dp[n][1], dp[n][2], dp[n][3])
    }
}
