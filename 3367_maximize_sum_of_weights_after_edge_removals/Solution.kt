// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

class Solution {
    private lateinit var g: Array<ArrayList<IntArray>>
    private var k = 0

    fun maximizeSumOfWeights(edges: Array<IntArray>, k: Int): Long {
        val n = edges.size + 1
        this.k = k
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
        }
        return dfs(0, -1)[1]
    }

    private fun dfs(u: Int, p: Int): LongArray {
        var base = 0L
        val gains = ArrayList<Long>()
        for (e in g[u]) {
            val to = e[0]
            val w = e[1]
            if (to == p) continue
            val child = dfs(to, u)
            base += child[1]
            val gain = child[0] + w - child[1]
            if (gain > 0) gains.add(gain)
        }
        gains.sortDescending()
        var with = base
        var without = base
        var i = 0
        while (i < gains.size && i < k - 1) {
            with += gains[i]
            i++
        }
        i = 0
        while (i < gains.size && i < k) {
            without += gains[i]
            i++
        }
        return longArrayOf(with, without)
    }
}
