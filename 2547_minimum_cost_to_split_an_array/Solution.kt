// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

class Solution {
    fun minCost(nums: IntArray, k: Int): Int {
        val n = nums.size
        val INF = 1_000_000_000_000_000_000L
        val dp = LongArray(n + 1) { INF }
        dp[0] = 0
        for (i in 0 until n) {
            val freq = HashMap<Int, Int>()
            var trimmed = 0
            for (j in i until n) {
                val c = (freq[nums[j]] ?: 0) + 1
                freq[nums[j]] = c
                if (c == 2) trimmed += 2
                else if (c > 2) trimmed += 1
                val cost = dp[i] + k + trimmed
                if (cost < dp[j + 1]) dp[j + 1] = cost
            }
        }
        return dp[n].toInt()
    }
}
