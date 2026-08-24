// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

class Solution {
    fun minimumCost(nums: IntArray, cost: IntArray, k: Int): Long {
        var n = nums.size
        var pn = LongArray(n + 1)
        var pc = LongArray(n + 1)
        for (i in 0 until n) {
            pn[i + 1] = pn[i] + nums[i]
            pc[i + 1] = pc[i] + cost[i]
        }
        val inf = 1L  shl  62
        var dp = LongArray(n + 1)
        dp.fill(0)
        for (i in 0 until n) { dp[i] = inf }
        for (i in n - 1 downTo 0) {
            for (j in i until n) {
                var cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1]
                if (cand < dp[i]) dp[i] = cand
            }
        }
        return dp[0]
    }
}
