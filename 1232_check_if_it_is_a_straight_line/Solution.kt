// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution {
    fun checkStraightLine(coordinates: Array<IntArray>): Boolean {
        val x0 = coordinates[0][0]
        val y0 = coordinates[0][1]
        val dx = coordinates[1][0] - x0
        val dy = coordinates[1][1] - y0
        for (i in 2 until coordinates.size) {
            val x = coordinates[i][0]
            val y = coordinates[i][1]
            if ((x - x0).toLong() * dy != (y - y0).toLong() * dx) return false
        }
        return true
    }
}
