// LeetCode 1401 - Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

class Solution {
    fun checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean {
        val x = minOf(maxOf(xCenter, x1), x2)
        val y = minOf(maxOf(yCenter, y1), y2)
        val dx = x - xCenter
        val dy = y - yCenter
        return dx * dx + dy * dy <= radius * radius
    }
}
