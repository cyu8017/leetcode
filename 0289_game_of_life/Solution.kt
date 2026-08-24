// LeetCode 0289 - Game of Life
// https://leetcode.com/problems/game-of-life/

class Solution {
    fun gameOfLife(board: Array<IntArray>) {
        val rows = board.size
        val cols = board[0].size
        for (row in 0 until rows) {
            for (col in 0 until cols) {
                var liveNeighbors = 0
                for (dr in -1..1) {
                    for (dc in -1..1) {
                        if (dr == 0 && dc == 0) {
                            continue
                        }
                        val nextRow = row + dr
                        val nextCol = col + dc
                        if (nextRow in 0 until rows && nextCol in 0 until cols && (board[nextRow][nextCol] and 1) == 1) {
                            liveNeighbors++
                        }
                    }
                }
                if ((board[row][col] and 1) == 1 && liveNeighbors in 2..3) {
                    board[row][col] = board[row][col] or 2
                } else if ((board[row][col] and 1) == 0 && liveNeighbors == 3) {
                    board[row][col] = board[row][col] or 2
                }
            }
        }
        for (row in 0 until rows) {
            for (col in 0 until cols) {
                board[row][col] = board[row][col] shr 1
            }
        }
    }
}
