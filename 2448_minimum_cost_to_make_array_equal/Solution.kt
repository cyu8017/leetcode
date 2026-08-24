// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

class Solution {
    fun minCost(nums: IntArray, cost: IntArray): Long {
        val n = nums.size
        val idx = Array(n) { it }
        idx.sortWith(compareBy { nums[it] })
        var totalCost = 0L
        for (c in cost) totalCost += c
        var pref = 0L
        var median = 0
        for (i in idx) {
            pref += cost[i]
            if (pref * 2 >= totalCost) {
                median = nums[i]
                break
            }
        }
        var ans = 0L
        for (i in 0 until n) {
            ans += kotlin.math.abs(nums[i] - median).toLong() * cost[i]
        }
        return ans
    }
}
