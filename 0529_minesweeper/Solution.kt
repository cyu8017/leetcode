// LeetCode 0529 - Minesweeper
// https://leetcode.com/problems/minesweeper/

class Solution {
    private val directions = arrayOf(
        intArrayOf(-1, -1), intArrayOf(-1, 0), intArrayOf(-1, 1),
        intArrayOf(0, -1), intArrayOf(0, 1),
        intArrayOf(1, -1), intArrayOf(1, 0), intArrayOf(1, 1),
    )

    fun updateBoard(board: Array<Array<String>>, click: IntArray): Array<Array<String>> {
        val row = click[0]
        val col = click[1]
        if (board[row][col] == "M") {
            board[row][col] = "X"
            return board
        }
        reveal(board, row, col)
        return board
    }

    private fun reveal(board: Array<Array<String>>, row: Int, col: Int) {
        if (row !in board.indices || col !in board[0].indices || board[row][col] != "E") {
            return
        }
        val mines = countMines(board, row, col)
        board[row][col] = if (mines == 0) "B" else mines.toString()
        if (mines == 0) {
            for ((dr, dc) in directions) {
                reveal(board, row + dr, col + dc)
            }
        }
    }

    private fun countMines(board: Array<Array<String>>, row: Int, col: Int): Int {
        var total = 0
        for ((dr, dc) in directions) {
            val nextRow = row + dr
            val nextCol = col + dc
            if (nextRow in board.indices && nextCol in board[0].indices && board[nextRow][nextCol] == "M") {
                total++
            }
        }
        return total
    }
}
