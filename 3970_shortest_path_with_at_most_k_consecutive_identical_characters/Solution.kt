// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

class Solution {
    fun shortestPath(n: Int, edges: Array<IntArray>, labels: String, k: Int): Long {
        val graph = Array(n) { ArrayList<IntArray>() }
        for (edge in edges) graph[edge[0]].add(intArrayOf(edge[1], edge[2]))
        val infinity = Long.MAX_VALUE / 4
        val distances = Array(n) { LongArray(k + 1) { infinity } }
        distances[0][1] = 0
        val pq = java.util.PriorityQueue<LongArray>(compareBy { it[0] })
        pq.offer(longArrayOf(0, 0, 1))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val distance = cur[0]
            val node = cur[1].toInt()
            val run = cur[2].toInt()
            if (distance != distances[node][run]) continue
            if (node == n - 1) return distance
            for (e in graph[node]) {
                val to = e[0]
                val weight = e[1]
                var nextRun = 1
                if (labels[node] == labels[to]) nextRun = run + 1
                if (nextRun > k) continue
                val nextDistance = distance + weight
                if (nextDistance < distances[to][nextRun]) {
                    distances[to][nextRun] = nextDistance
                    pq.offer(longArrayOf(nextDistance, to.toLong(), nextRun.toLong()))
                }
            }
        }
        return -1
    }
}
