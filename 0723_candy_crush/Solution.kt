// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

class Solution {
    fun candyCrush(board: Array<IntArray>): Array<IntArray> {
        var m = board.size
        var n = board[0].size
        var stable = false
        while (!stable) {
            stable = true
            for (i in 0 until m) {
                for (j in 0 until n - 2) {
                    var value = kotlin.math.abs(board[i][j])
                    if (value != 0 && value == kotlin.math.abs(board[i][j + 1]) && value == kotlin.math.abs(board[i][j + 2])) {
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -value
                        stable = false
                    }
                }
            }
            for (j in 0 until n) {
                for (i in 0 until m - 2) {
                    var value = kotlin.math.abs(board[i][j])
                    if (value != 0 && value == kotlin.math.abs(board[i + 1][j]) && value == kotlin.math.abs(board[i + 2][j])) {
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -value
                        stable = false
                    }
                }
            }
            for (j in 0 until n) {
                var write = m - 1
                for (i in m - 1 downTo 0) {
                    if (board[i][j] > 0) board[write--][j] = board[i][j]
                }
                run {
                    var i = write
                    while (i >= 0) {
                        board[i][j] = 0
                        i--
                    }
                }
            }
        }
        return board
    }
}
