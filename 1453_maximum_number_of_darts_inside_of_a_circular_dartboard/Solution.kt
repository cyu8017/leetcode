// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

import kotlin.math.sqrt

class Solution {
    fun numPoints(darts: Array<IntArray>, r: Int): Int {
        var ans = if (darts.isNotEmpty()) 1 else 0
        val rr = r.toDouble() * r
        for (i in darts.indices) {
            for (j in i + 1 until darts.size) {
                val x1 = darts[i][0].toDouble()
                val y1 = darts[i][1].toDouble()
                val x2 = darts[j][0].toDouble()
                val y2 = darts[j][1].toDouble()
                val dx = x2 - x1
                val dy = y2 - y1
                val d2 = dx * dx + dy * dy
                if (d2 > 4 * rr || d2 == 0.0) continue
                val d = sqrt(d2)
                val h = sqrt(rr - d2 / 4)
                val mx = (x1 + x2) / 2
                val my = (y1 + y2) / 2
                for (sign in intArrayOf(-1, 1)) {
                    val cx = mx + sign * (-dy) * h / d
                    val cy = my + sign * dx * h / d
                    var count = 0
                    for (p in darts) {
                        val px = p[0] - cx
                        val py = p[1] - cy
                        if (px * px + py * py <= rr + 1e-7) count++
                    }
                    ans = maxOf(ans, count)
                }
            }
        }
        return ans
    }
}
