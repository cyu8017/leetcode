// LeetCode 2662 - Minimum Cost of a Path With Special Roads
// https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

class Solution {
    fun minimumCost(start: IntArray, target: IntArray, specialRoads: Array<IntArray>): Int {
        val points = ArrayList<IntArray>()
        points.add(start)
        points.add(target)
        for (r in specialRoads) {
            points.add(intArrayOf(r[0], r[1]))
            points.add(intArrayOf(r[2], r[3]))
        }
        val N = points.size
        val g = Array(N) { ArrayList<IntArray>() }
        for (i in 0 until N)
            for (j in 0 until N)
                if (i != j) g[i].add(intArrayOf(j, man(points[i], points[j])))
        for (r in specialRoads) {
            var u = -1
            var v = -1
            for (i in 0 until N) {
                val p = points[i]
                if (p[0] == r[0] && p[1] == r[1]) u = i
                if (p[0] == r[2] && p[1] == r[3]) v = i
            }
            if (u >= 0 && v >= 0) g[u].add(intArrayOf(v, r[4]))
        }
        val dist = IntArray(N) { Int.MAX_VALUE / 4 }
        dist[0] = 0
        val pq = java.util.PriorityQueue<IntArray>(compareBy { it[1] })
        pq.offer(intArrayOf(0, 0))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            val id = cur[0]
            val cost = cur[1]
            if (cost > dist[id]) continue
            for (e in g[id]) {
                if (cost + e[1] < dist[e[0]]) {
                    dist[e[0]] = cost + e[1]
                    pq.offer(intArrayOf(e[0], dist[e[0]]))
                }
            }
        }
        return dist[1]
    }

    private fun man(a: IntArray, b: IntArray): Int =
        kotlin.math.abs(a[0] - b[0]) + kotlin.math.abs(a[1] - b[1])
}
