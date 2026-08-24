// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private var n = 0

    private fun bfs(start: Int): Pair<Int, IntArray> {
        val dist = IntArray(n) { -1 }
        val q = ArrayDeque<Int>()
        q.add(start)
        dist[start] = 0
        var far = start
        while (q.isNotEmpty()) {
            val u = q.removeFirst()
            if (dist[u] > dist[far]) far = u
            for (v in g[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1
                    q.add(v)
                }
            }
        }
        return far to dist
    }

    fun lastMarkedNodes(edges: Array<IntArray>): IntArray {
        n = edges.size + 1
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val u = bfs(0).first
        val (v, du) = run {
            val ru = bfs(u)
            ru.first to ru.second
        }
        val dv = bfs(v).second
        val ans = IntArray(n)
        for (i in 0 until n) ans[i] = if (du[i] >= dv[i]) u else v
        return ans
    }
}
