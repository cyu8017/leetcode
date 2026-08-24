// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find_diameter_endpoints_of_a_tree/

class Solution {
    private lateinit var g: Array<ArrayList<Int>>
    private var n = 0

    fun findSpecialNodes(n: Int, edges: Array<IntArray>): String {
        this.n = n
        g = Array(n) { ArrayList() }
        for (e in edges) {
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        }
        val r0 = bfs(0)
        val a = r0[0]
        val r1 = bfs(a)
        val b = r1[0]
        val dist1 = r1.copyOfRange(1, n + 1)
        val r2 = bfs(b)
        val dist2 = r2.copyOfRange(1, n + 1)
        val d = dist1[b]
        val ans = CharArray(n) { '0' }
        for (i in 0 until n) {
            if (dist1[i] == d || dist2[i] == d) ans[i] = '1'
        }
        return String(ans)
    }

    private fun bfs(start: Int): IntArray {
        val dist = IntArray(n) { -1 }
        dist[start] = 0
        val q = ArrayList<Int>()
        q.add(start)
        var far = start
        var head = 0
        while (head < q.size) {
            val u = q[head++]
            if (dist[u] > dist[far]) far = u
            for (v in g[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1
                    q.add(v)
                }
            }
        }
        val out = IntArray(n + 1)
        out[0] = far
        System.arraycopy(dist, 0, out, 1, n)
        return out
    }
}
