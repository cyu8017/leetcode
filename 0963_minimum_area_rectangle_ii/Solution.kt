// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

class Solution {
    fun minAreaFreeRect(points: Array<IntArray>): Double {
        val n = points.size
        val groups = HashMap<String, MutableList<IntArray>>()
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val cx = points[i][0].toLong() + points[j][0]
                val cy = points[i][1].toLong() + points[j][1]
                val dx = points[i][0].toLong() - points[j][0]
                val dy = points[i][1].toLong() - points[j][1]
                val dist = dx * dx + dy * dy
                val key = "$cx#$cy#$dist"
                groups.getOrPut(key) { mutableListOf() }.add(intArrayOf(i, j))
            }
        }
        var ans = 1e300
        for (pairs in groups.values) {
            for (a in pairs.indices) {
                for (b in a + 1 until pairs.size) {
                    val p1 = pairs[a][0]
                    val p2 = pairs[b][0]
                    val q2 = pairs[b][1]
                    val d1 = hypot(points[p1][0] - points[p2][0], points[p1][1] - points[p2][1])
                    val d2 = hypot(points[p1][0] - points[q2][0], points[p1][1] - points[q2][1])
                    val area = d1 * d2
                    if (area > 0) ans = minOf(ans, area)
                }
            }
        }
        return if (ans >= 1e299) 0.0 else ans
    }

    private fun hypot(x: Int, y: Int): Double =
        kotlin.math.sqrt(x.toDouble() * x + y.toDouble() * y)
}
