// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

class Solution {
    fun minCost(costs: Array<IntArray>): Int {
        if (costs.isEmpty()) {
            return 0
        }
        var previous = costs[0].clone()
        for (row in 1 until costs.size) {
            previous = intArrayOf(
                costs[row][0] + minOf(previous[1], previous[2]),
                costs[row][1] + minOf(previous[0], previous[2]),
                costs[row][2] + minOf(previous[0], previous[1]),
            )
        }
        return previous.minOrNull() ?: 0
    }
}
