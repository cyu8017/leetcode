// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

class Solution {
    fun minCostToSupplyWater(n: Int, wells: IntArray, pipes: Array<IntArray>): Int {
        val parent = IntArray(n + 1) { it }
        fun find(x: Int): Int {
            var cur = x
            while (parent[cur] != cur) {
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            }
            return cur
        }
        val edges = mutableListOf<IntArray>()
        for (i in wells.indices) edges.add(intArrayOf(0, i + 1, wells[i]))
        for (p in pipes) edges.add(p)
        edges.sortBy { it[2] }
        var ans = 0
        for (e in edges) {
            val ra = find(e[0])
            val rb = find(e[1])
            if (ra == rb) continue
            parent[rb] = ra
            ans += e[2]
        }
        return ans
    }
}
