// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/


class Solution {
    fun judgeCircle(moves: String): Boolean {
        var x = 0
        var y = 0
        for (ch in moves) {
            when (ch) {
                'U' -> y++
                'D' -> y--
                'L' -> x--
                'R' -> x++
            }
        }
        return x == 0 && y == 0
    }
}
