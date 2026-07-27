// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

import kotlin.math.PI
import kotlin.math.atan2

class Solution {
    fun visiblePoints(points: List<List<Int>>, angle: Int, location: List<Int>): Int {
        var same = 0
        val a = mutableListOf<Double>()
        val lx = location[0]
        val ly = location[1]
        for (p in points) {
            val dx = p[0] - lx
            val dy = p[1] - ly
            if (dx == 0 && dy == 0) same++
            else a.add(atan2(dy.toDouble(), dx.toDouble()))
        }
        a.sort()
        val ext = a + a.map { it + 2 * PI }
        val width = Math.toRadians(angle.toDouble()) + 1e-12
        var left = 0
        var best = 0
        for (right in ext.indices) {
            while (ext[right] - ext[left] > width) left++
            best = maxOf(best, minOf(a.size, right - left + 1))
        }
        return best + same
    }
}
