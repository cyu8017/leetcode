// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

class Solution {
    private lateinit var points: Array<IntArray>
    private var n = 0

    private fun dist(i: Int, j: Int): Int =
        kotlin.math.abs(points[i][0] - points[j][0]) + kotlin.math.abs(points[i][1] - points[j][1])

    private fun ok(d: Int): Boolean {
        val g = Array(n) { ArrayList<Int>() }
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (dist(i, j) < d) {
                    g[i].add(j)
                    g[j].add(i)
                }
            }
        }
        val color = IntArray(n) { -1 }
        for (i in 0 until n) {
            if (color[i] != -1) continue
            val q = ArrayDeque<Int>()
            q.offer(i)
            color[i] = 0
            while (q.isNotEmpty()) {
                val u = q.poll()
                for (v in g[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] xor 1
                        q.offer(v)
                    } else if (color[v] == color[u]) return false
                }
            }
        }
        return true
    }

    fun maxPartitionFactor(points: Array<IntArray>): Int {
        this.points = points
        n = points.size
        if (n == 2) return 0
        var lo = 0
        var hi = 0
        for (i in 0 until n) {
            for (j in i + 1 until n) hi = maxOf(hi, dist(i, j))
        }
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (ok(mid)) lo = mid
            else hi = mid - 1
        }
        return lo
    }
}
