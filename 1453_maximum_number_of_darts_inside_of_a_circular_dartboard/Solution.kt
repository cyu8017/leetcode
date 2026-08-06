// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

import kotlin.math.sqrt

class Solution {
    fun numPoints(darts: Array<IntArray>, r: Int): Int {
        var ans = if (darts.isEmpty()) 0 else 1
        for (i in darts.indices) {
            val x1 = darts[i][0]
            val y1 = darts[i][1]
            for (j in i + 1 until darts.size) {
                val x2 = darts[j][0]
                val y2 = darts[j][1]
                val dx = (x2 - x1).toDouble()
                val dy = (y2 - y1).toDouble()
                val d2 = dx * dx + dy * dy
                if (d2 > 4.0 * r * r || d2 == 0.0) continue
                val d = sqrt(d2)
                val h = sqrt(r.toDouble() * r - d2 / 4)
                val mx = (x1 + x2) / 2.0
                val my = (y1 + y2) / 2.0
                for (sign in intArrayOf(-1, 1)) {
                    val cx = mx + sign * (-dy) * h / d
                    val cy = my + sign * dx * h / d
                    var count = 0
                    for (p in darts) {
                        val px = p[0] - cx
                        val py = p[1] - cy
                        if (px * px + py * py <= r.toDouble() * r + 1e-7) count++
                    }
                    ans = maxOf(ans, count)
                }
            }
        }
        return ans
    }
}
