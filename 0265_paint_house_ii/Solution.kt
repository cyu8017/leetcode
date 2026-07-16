// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

class Solution {
    fun minCostII(costs: Array<IntArray>): Int {
        if (costs.isEmpty()) {
            return 0
        }
        val colorCount = costs[0].size
        var previous = costs[0].copyOf()
        for (row in 1 until costs.size) {
            val minCost = previous.minOrNull()!!
            val minIndex = previous.indexOf(minCost)
            val secondMin = previous.filterIndexed { index, _ -> index != minIndex }.minOrNull()!!
            val current = IntArray(colorCount)
            for (color in 0 until colorCount) {
                val extra = if (color == minIndex) secondMin else minCost
                current[color] = costs[row][color] + extra
            }
            previous = current
        }
        return previous.minOrNull()!!
    }
}
