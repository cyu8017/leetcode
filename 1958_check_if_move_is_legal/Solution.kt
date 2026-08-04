// LeetCode 1958
// https://leetcode.com/problems/check-if-move-is-legal/

class Solution {
    fun checkMove(board: Array<CharArray>, rMove: Int, cMove: Int, color: Char): Boolean {
        val opp = if (color == 'B') 'W' else 'B'
        val dirs = arrayOf(
            intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1),
            intArrayOf(1, 1), intArrayOf(1, -1), intArrayOf(-1, 1), intArrayOf(-1, -1)
        )
        for (dir in dirs) {
            var r = rMove + dir[0]
            var c = cMove + dir[1]
            var steps = 0
            while (r in 0 until 8 && c in 0 until 8 && board[r][c] == opp) {
                r += dir[0]
                c += dir[1]
                steps++
            }
            if (steps > 0 && r in 0 until 8 && c in 0 until 8 && board[r][c] == color) return true
        }
        return false
    }
}
