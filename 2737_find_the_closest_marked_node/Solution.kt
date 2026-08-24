// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

import java.util.PriorityQueue

class Solution {
    fun minimumDistance(n: Int, edges: Array<IntArray>, s: Int, marked: IntArray): Int {
        val g = Array(n) { ArrayList<IntArray>() }
        for (e in edges) g[e[0]].add(intArrayOf(e[1], e[2]))
        val mark = HashSet<Int>()
        for (x in marked) mark.add(x)
        val dist = IntArray(n) { Int.MAX_VALUE / 4 }
        dist[s] = 0
        val pq = PriorityQueue(compareBy<IntArray> { it[0] })
        pq.offer(intArrayOf(0, s))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val d = cur[0]
            val u = cur[1]
            if (mark.contains(u)) return d
            if (d > dist[u]) continue
            for (vw in g[u]) {
                val v = vw[0]
                val w = vw[1]
                if (d + w < dist[v]) {
                    dist[v] = d + w
                    pq.offer(intArrayOf(dist[v], v))
                }
            }
        }
        return -1
    }
}
