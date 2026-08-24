// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

class Solution {
    fun finalPositionOfSnake(n: Int, commands: Array<String>): Int {
        var x = 0
        var y = 0
        for (c in commands) {
            when (c[0]) {
                'U' -> x--
                'D' -> x++
                'L' -> y--
                'R' -> y++
            }
        }
        return x * n + y
    }
}
