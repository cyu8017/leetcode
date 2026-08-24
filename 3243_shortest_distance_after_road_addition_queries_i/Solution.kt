// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

class Solution {
    fun shortestDistanceAfterQueries(n: Int, queries: Array<IntArray>): IntArray {
        val g = Array(n) { ArrayList<Int>() }
        for (i in 0 until n - 1) g[i].add(i + 1)
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            g[queries[i][0]].add(queries[i][1])
            ans[i] = bfs(g, n, 0)
        }
        return ans
    }

    private fun bfs(g: Array<ArrayList<Int>>, n: Int, start: Int): Int {
        val q = ArrayDeque<Int>()
        q.add(start)
        val vis = BooleanArray(n)
        vis[start] = true
        var d = 0
        while (true) {
            var k = q.size
            while (k-- > 0) {
                val u = q.removeFirst()
                if (u == n - 1) return d
                for (v in g[u]) {
                    if (!vis[v]) {
                        vis[v] = true
                        q.add(v)
                    }
                }
            }
            d++
        }
    }
}
