// LeetCode 1029 - Two City Scheduling
// https://leetcode.com/problems/two-city-scheduling/

class Solution {
    fun twoCitySchedCost(costs: Array<IntArray>): Int {
        costs.sortBy { it[0] - it[1] }
        val n = costs.size / 2
        var sum = 0
        for (i in 0 until n) sum += costs[i][0]
        for (i in n until costs.size) sum += costs[i][1]
        return sum
    }
}
