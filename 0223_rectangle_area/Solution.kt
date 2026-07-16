// LeetCode 0223 - Rectangle Area
// https://leetcode.com/problems/rectangle-area/

class Solution {
    fun computeArea(ax1: Int, ay1: Int, ax2: Int, ay2: Int, bx1: Int, by1: Int, bx2: Int, by2: Int): Int {
        val areaA = (ax2 - ax1) * (ay2 - ay1)
        val areaB = (bx2 - bx1) * (by2 - by1)
        val overlapW = maxOf(0, minOf(ax2, bx2) - maxOf(ax1, bx1))
        val overlapH = maxOf(0, minOf(ay2, by2) - maxOf(ay1, by1))
        return areaA + areaB - overlapW * overlapH
    }
}
