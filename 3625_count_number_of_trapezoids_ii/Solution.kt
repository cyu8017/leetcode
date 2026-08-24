// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

class Solution {
    fun countTrapezoids(points: Array<IntArray>): Int {
        val n = points.size
        val cnt1 = HashMap<Double, HashMap<Double, Int>>()
        val cnt2 = HashMap<Int, HashMap<Double, Int>>()
        for (i in 0 until n) {
            val x1 = points[i][0]
            val y1 = points[i][1]
            for (j in 0 until i) {
                val x2 = points[j][0]
                val y2 = points[j][1]
                val dx = x2 - x1
                val dy = y2 - y1
                val k: Double
                val b: Double
                if (dx == 0) {
                    k = 1e9
                    b = x1.toDouble()
                } else {
                    k = dy.toDouble() / dx
                    b = (y1.toLong() * dx - x1.toLong() * dy).toDouble() / dx
                }
                cnt1.getOrPut(k) { HashMap() }.merge(b, 1) { a, c -> a + c }
                val p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                cnt2.getOrPut(p) { HashMap() }.merge(k, 1) { a, c -> a + c }
            }
        }
        var ans = 0
        for (e in cnt1.values) {
            var s = 0
            for (t in e.values) {
                ans += s * t
                s += t
            }
        }
        for (e in cnt2.values) {
            var s = 0
            for (t in e.values) {
                ans -= s * t
                s += t
            }
        }
        return ans
    }
}
