// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private var n = 0

    private fun bfsDepth(start: Int): Int {
        val dist = IntArray(n + 1) { -1 }
        val q = ArrayDeque<Int>()
        q.add(start)
        dist[start] = 1
        var best = 1
        while (q.isNotEmpty()) {
            val u = q.removeFirst()
            if (dist[u] > best) best = dist[u]
            for (v in g[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1
                    q.add(v)
                }
            }
        }
        return best
    }

    fun magnificentSets(n: Int, edges: Array<IntArray>): Int {
        this.n = n
        g = Array(n + 1) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val color = IntArray(n + 1) { -1 }
        val components = ArrayList<List<Int>>()
        for (i in 1..n) {
            if (color[i] != -1) continue
            val comp = ArrayList<Int>()
            val q = ArrayDeque<Int>()
            q.add(i)
            color[i] = 0
            var bipartite = true
            while (q.isNotEmpty()) {
                val u = q.removeFirst()
                comp.add(u)
                for (v in g[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] xor 1
                        q.add(v)
                    } else if (color[v] == color[u]) {
                        bipartite = false
                    }
                }
            }
            if (!bipartite) return -1
            components.add(comp)
        }
        var ans = 0
        for (comp in components) {
            var best = 0
            for (u in comp) best = maxOf(best, bfsDepth(u))
            ans += best
        }
        return ans
    }
}
