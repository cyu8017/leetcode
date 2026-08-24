// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

class Solution {
    fun minCostToEqualizeArray(nums: IntArray, cost1: Int, cost2: Int): Int {
        val MOD = 1_000_000_007
        var n = nums.size
        var minNum = nums[0]
        var maxNum = nums[0]
        var sum = 0
        for (v in nums) {
            minNum = minOf(minNum, v)
            maxNum = maxOf(maxNum, v)
            sum += v
        }
        if (cost1 * 2L <= cost2 || n < 3) {
            var totalGap = 1L * maxNum * n - sum
            return (1L * cost1 * totalGap % MOD)
        }
        var ans = Long.MAX_VALUE
        for (target in maxNum until 2 * maxNum) {
            var maxGap = target - minNum
            var totalGap = 1L * target * n - sum
            var pairs = totalGap / 2
            var alt = totalGap - maxGap
            if (alt < pairs) pairs = alt
            var cost = 1L * cost1 * (totalGap - 2 * pairs) + 1L * cost2 * pairs
            ans = minOf(ans, cost)
        }
        return (ans % MOD)
    }
}
