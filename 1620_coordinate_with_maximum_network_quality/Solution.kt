// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

import kotlin.math.hypot

class Solution {
    fun bestCoordinate(towers: Array<IntArray>, radius: Int): IntArray {
        var best = intArrayOf(0, 0)
        var quality = -1
        for (x in 0..50) {
            for (y in 0..50) {
                var q = 0
                for (t in towers) {
                    val d = hypot((x - t[0]).toDouble(), (y - t[1]).toDouble())
                    if (d <= radius) q += (t[2] / (1 + d)).toInt()
                }
                if (q > quality) {
                    quality = q
                    best = intArrayOf(x, y)
                }
            }
        }
        return best
    }
}
