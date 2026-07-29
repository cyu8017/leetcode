// LeetCode 1041 - Robot Bounded In Circle
// https://leetcode.com/problems/robot-bounded-in-circle/

class Solution {
    fun isRobotBounded(instructions: String): Boolean {
        var x = 0; var y = 0; var dx = 0; var dy = 1
        for (ch in instructions) {
            when (ch) {
                'G' -> { x += dx; y += dy }
                'L' -> { val tmp = dx; dx = -dy; dy = tmp }
                else -> { val tmp = dx; dx = dy; dy = -tmp }
            }
        }
        return (x == 0 && y == 0) || !(dx == 0 && dy == 1)
    }
}
