// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution {
    fun minimumCost(cost1: Int, cost2: Int, costBoth: Int, need1: Int, need2: Int): Long {
        var a = need1 * cost1 + need2 * cost2
        var b = costBoth * maxOf(need1, need2)
        var mn = minOf(need1, need2)
        var c = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        return minOf(a, minOf(b, c))
    }
}
