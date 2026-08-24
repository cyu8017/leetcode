// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private lateinit var vis: BooleanArray

    fun countPairs(n: Int, edges: Array<IntArray>): Long {
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        vis = BooleanArray(n)
        var ans = 0L
        var seen = 0L
        for (i in 0 until n) {
            if (!vis[i]) {
                val sz = dfs(i).toLong()
                ans += sz * seen
                seen += sz
            }
        }
        return ans
    }

    private fun dfs(u: Int): Int {
        vis[u] = true
        var size = 1
        for (v in g[u]) if (!vis[v]) size += dfs(v)
        return size
    }
}
