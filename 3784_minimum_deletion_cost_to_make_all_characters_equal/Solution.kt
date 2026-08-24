// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum_deletion_cost_to_make_all_characters_equal/

class Solution {
    fun minCost(s: String, cost: IntArray): Long {
        var tot = 0L
        val g = HashMap<Char, Long>()
        for (i in cost.indices) {
            tot += cost[i]
            g[s[i]] = g.getOrDefault(s[i], 0L) + cost[i]
        }
        var ans = tot
        for (x in g.values) {
            ans = minOf(ans, tot - x)
        }
        return ans
    }
}
