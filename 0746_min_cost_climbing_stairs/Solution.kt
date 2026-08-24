// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution {
    fun minCostClimbingStairs(cost: IntArray): Int {
        var a = 0
        var b = 0
        for (i in cost.size - 1 downTo 0) {
            var nextA = cost[i] + minOf(a, b)
            b = a
            a = nextA
        }
        return minOf(a, b)
    }
}
