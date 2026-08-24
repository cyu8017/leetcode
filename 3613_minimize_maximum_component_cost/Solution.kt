// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

class Solution {
    private lateinit var p: IntArray

    private fun find(x: Int): Int {
        if (p[x] != x) p[x] = find(p[x])
        return p[x]
    }

    fun minCost(n: Int, edges: Array<IntArray>, k: Int): Int {
        p = IntArray(n) { it }
        if (k == n) return 0
        edges.sortBy { it[2] }
        var cnt = n
        for (e in edges) {
            val pu = find(e[0])
            val pv = find(e[1])
            if (pu != pv) {
                p[pu] = pv
                cnt--
                if (cnt <= k) return e[2]
            }
        }
        return 0
    }
}
