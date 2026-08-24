// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

class Solution {
    fun findAnswer(n: Int, edges: Array<IntArray>): BooleanArray {
        @SuppressWarnings("unchecked")
        List<int[]>[] g = ArrayList[n]
        for (i in 0 until n) { g[i] = ArrayList() }
        for (i in 0 until edges.size) {
            var a = edges[i][0]
            var b = edges[i][1]
            var w = edges[i][2]
            g[a].add(intArrayOf(b, w, i))
            g[b].add(intArrayOf(a, w, i))
        }
        val INF = 1  shl  30
        var dist = IntArray(n)
        dist.fill(INF)
        dist[0] = 0
        var pq = PriorityQueue((a, b) -> a[0] - b[0])
        pq.offer(intArrayOf(0, 0))
        while (!pq.isEmpty()) {
            var cur = pq.poll()
            var da = cur[0]
            var a = cur[1]
            if (da > dist[a]) continue
            for (e in g[a]) {
                var b = e[0]
                var w = e[1]
                if (dist[b] > dist[a] + w) {
                    dist[b] = dist[a] + w
                    pq.offer(intArrayOf(dist[b], b))
                }
            }
        }
        var ans = BooleanArray(edges.size)
        if (dist[n - 1] == INF) return ans
        var q = ArrayDeque<Int>()
        q.offer(n - 1)
        while (!q.isEmpty()) {
            var a = q.poll()
            for (e in g[a]) {
                var b = e[0]
                var w = e[1]
                var i = e[2]
                if (dist[a] == dist[b] + w) {
                    ans[i] = true
                    q.offer(b)
                }
            }
        }
        return ans
    }
}
