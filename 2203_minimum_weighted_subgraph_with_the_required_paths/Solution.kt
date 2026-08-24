// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

class Solution {

    private fun dijkstra(n: Int, g: Array<Array<MutableList<Int>>>, src: Int): LongArray {

            var INF = 1L << 62
            var dist = LongArray(n)
            dist.fill(INF)
            dist[src] = 0
            var pq = PriorityQueue({ a, b -> Long.compare(a[0], b[0] }))
            pq.offer(longArrayOf(0, src))
            while (!pq.isEmpty()) {
                var cur = pq.poll()
                var d = cur[0]
                var u = cur.toInt()[1]
                if (d != dist[u]) continue
                for (e in g[u]) {
                    var v = e[0]; var w = e[1]
                    if (d + w < dist[v]) {
                        dist[v] = d + w
                        pq.offer(longArrayOf(dist[v], v))
                    }
                }
            }
            return dist

    }


    fun minimumWeight(n: Int, edges: Array<IntArray>, src1: Int, src2: Int, dest: Int): Long {

            @SuppressWarnings("unchecked")
            var g = arrayOfNulls<ArrayList>(n)
            @SuppressWarnings("unchecked")
            var rg = arrayOfNulls<ArrayList>(n)
            for (i in 0 until n) {
                g[i] = ArrayList<Int>()
                rg[i] = ArrayList<Int>()
            }
            for (e in edges) {
                g[e[0]].add(intArrayOf(e[1], e[2]))
                rg[e[1]].add(intArrayOf(e[0], e[2]))
            }
            var d1 = dijkstra(n, g, src1)
            var d2 = dijkstra(n, g, src2)
            var dd = dijkstra(n, rg, dest)
            var INF = 1L << 62
            var ans = INF
            for (i in 0 until n) {
                if (d1[i] >= INF || d2[i] >= INF || dd[i] >= INF) continue
                ans = minOf(ans, d1[i] + d2[i] + dd[i])
            }
            return ans >= if (INF) -1 else ans

    }

}
