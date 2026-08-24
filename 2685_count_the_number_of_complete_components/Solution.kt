// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution {
    fun countCompleteComponents(n: Int, edges: Array<IntArray>): Int {
        val g = Array(n) { ArrayList<Int>() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val vis = BooleanArray(n)
        var ans = 0
        for (i in 0 until n) {
            if (vis[i]) continue
            val nodes = ArrayList<Int>()
            dfs(g, vis, i, nodes)
            var ecount = 0
            for (u in nodes) ecount += g[u].size
            ecount /= 2
            val sz = nodes.size
            if (ecount == sz * (sz - 1) / 2) ans++
        }
        return ans
    }

    private fun dfs(g: Array<ArrayList<Int>>, vis: BooleanArray, u: Int, nodes: ArrayList<Int>) {
        vis[u] = true
        nodes.add(u)
        for (v in g[u]) if (!vis[v]) dfs(g, vis, v, nodes)
    }
}
