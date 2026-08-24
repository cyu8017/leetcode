// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/


class Solution {
    private lateinit var g: Array<MutableList<Int>>
    private lateinit var values: IntArray

    fun maximumScoreAfterOperations(edges: Array<IntArray>, values: IntArray): Long {
        val n = values.size
        this.values = values
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        var total = 0L
        for (v in values) total += v
        return total - dfs(0, -1)
    }

    private fun dfs(u: Int, p: Int): Long {
        var sumKids = 0L
        var isLeaf = true
        for (v in g[u]) {
            if (v == p) continue
            isLeaf = false
            sumKids += dfs(v, u)
        }
        if (isLeaf) return values[u].toLong()
        return minOf(values[u].toLong(), sumKids)
    }
}
