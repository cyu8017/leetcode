// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

class Solution {
    private lateinit var g: Array<ArrayList<IntArray>>

    fun maxScore(edges: Array<IntArray>): Long {
        val n = edges.size + 1
        g = Array(n) { ArrayList() }
        for (i in 1 until n) {
            val p = edges[i - 1][0]
            val w = edges[i - 1][1]
            g[p].add(intArrayOf(i, w))
            g[i].add(intArrayOf(p, w))
        }
        return dfs(0, -1)[0]
    }

    private fun dfs(u: Int, p: Int): LongArray {
        var base = 0L
        var bestGain = 0L
        for (e in g[u]) {
            val to = e[0]
            val w = e[1]
            if (to == p) continue
            val child = dfs(to, u)
            base += child[0]
            val gain = child[1] + w - child[0]
            if (gain > bestGain) bestGain = gain
        }
        return longArrayOf(base + bestGain, base)
    }
}
