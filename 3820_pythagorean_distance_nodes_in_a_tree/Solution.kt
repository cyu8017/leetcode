// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean_distance_nodes_in_a_tree/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private var n = 0

    fun specialNodes(n: Int, edges: Array<IntArray>, x: Int, y: Int, z: Int): Int {
        this.n = n
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val d1 = bfs(x)
        val d2 = bfs(y)
        val d3 = bfs(z)
        var ans = 0
        for (i in 0 until n) {
            val a = intArrayOf(d1[i], d2[i], d3[i])
            a.sort()
            val x0 = a[0].toLong()
            val x1 = a[1].toLong()
            val x2 = a[2].toLong()
            if (x0 * x0 + x1 * x1 == x2 * x2) ans++
        }
        return ans
    }

    private fun bfs(start: Int): IntArray {
        val dist = IntArray(n) { 1_000_000_000 }
        val q = ArrayDeque<Int>()
        dist[start] = 0
        q.add(start)
        while (q.isNotEmpty()) {
            val u = q.removeFirst()
            for (v in g[u]) {
                if (dist[v] > dist[u] + 1) {
                    dist[v] = dist[u] + 1
                    q.add(v)
                }
            }
        }
        return dist
    }
}
