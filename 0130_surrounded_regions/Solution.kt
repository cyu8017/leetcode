// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

class Solution {
    fun solve(board: Array<CharArray>) {
        if (board.isEmpty() || board[0].isEmpty()) return
        val rows = board.size
        val cols = board[0].size
        fun mark(r: Int, c: Int) {
            if (r !in 0 until rows || c !in 0 until cols || board[r][c] != 'O') return
            board[r][c] = 'E'
            mark(r + 1, c)
            mark(r - 1, c)
            mark(r, c + 1)
            mark(r, c - 1)
        }
        for (r in 0 until rows) {
            mark(r, 0)
            mark(r, cols - 1)
        }
        for (c in 0 until cols) {
            mark(0, c)
            mark(rows - 1, c)
        }
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                board[r][c] = when (board[r][c]) {
                    'O' -> 'X'
                    'E' -> 'O'
                    else -> board[r][c]
                }
            }
        }
    }
}