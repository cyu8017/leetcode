// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

import kotlin.math.hypot

class Solution {
    fun getMinDistSum(positions: Array<IntArray>): Double {
        var x = 0.0
        var y = 0.0
        for (position in positions) {
            x += position[0]
            y += position[1]
        }
        x /= positions.size
        y /= positions.size

        run loop@{
            repeat(10000) {
                var numeratorX = 0.0
                var numeratorY = 0.0
                var denominator = 0.0
                var coincident: DoubleArray? = null
                for (position in positions) {
                    val px = position[0].toDouble()
                    val py = position[1].toDouble()
                    val d = hypot(x - px, y - py)
                    if (d < 1e-12) {
                        coincident = doubleArrayOf(px, py)
                        break
                    }
                    numeratorX += px / d
                    numeratorY += py / d
                    denominator += 1.0 / d
                }
                val nx: Double
                val ny: Double
                if (coincident != null) {
                    nx = coincident[0]
                    ny = coincident[1]
                } else {
                    nx = numeratorX / denominator
                    ny = numeratorY / denominator
                }
                if (hypot(nx - x, ny - y) < 1e-8) {
                    x = nx
                    y = ny
                    return@loop
                }
                x = nx
                y = ny
            }
        }

        var total = 0.0
        for (position in positions) {
            total += hypot(x - position[0], y - position[1])
        }
        return total
    }
}
