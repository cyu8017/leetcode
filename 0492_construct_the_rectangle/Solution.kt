// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

import kotlin.math.sqrt

class Solution {
    fun constructRectangle(area: Int): IntArray {
        val limit = sqrt(area.toDouble()).toInt()
        for (width in limit downTo 1) {
            if (area % width == 0) {
                return intArrayOf(area / width, width)
            }
        }
        return intArrayOf(area, 1)
    }
}
