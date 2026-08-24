// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

class Solution {
    fun minThreshold(n: Int, edges: Array<IntArray>, source: Int, target: Int, k: Int): Int {
        if (source == target) return 0
        val g = Array(n) { ArrayList<IntArray>() }
        var maxWeight = 0
        for (e in edges) {
            g[e[0]].add(intArrayOf(e[1], e[2]))
            g[e[1]].add(intArrayOf(e[0], e[2]))
            maxWeight = maxOf(maxWeight, e[2])
        }
        if (!can(n, g, source, target, k, maxWeight)) return -1
        var lo = 0
        var hi = maxWeight
        while (lo < hi) {
            val mid = lo + (hi - lo) / 2
            if (can(n, g, source, target, k, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun can(n: Int, g: Array<ArrayList<IntArray>>, source: Int, target: Int, k: Int, threshold: Int): Boolean {
        val inf = 1000000000
        val dist = IntArray(n) { inf }
        dist[source] = 0
        val dq = ArrayDeque<Int>()
        dq.addLast(source)
        while (dq.isNotEmpty()) {
            val u = dq.removeFirst()
            for (e in g[u]) {
                val to = e[0]
                val weight = e[1]
                val cost = if (weight > threshold) 1 else 0
                if (dist[u] + cost >= dist[to] || dist[u] + cost > k) continue
                dist[to] = dist[u] + cost
                if (cost == 0) dq.addFirst(to) else dq.addLast(to)
            }
        }
        return dist[target] <= k
    }
}
