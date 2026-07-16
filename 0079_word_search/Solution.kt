// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val rows = board.size
        val cols = board[0].size

        fun dfs(row: Int, col: Int, index: Int): Boolean {
            if (index == word.length) {
                return true
            }
            if (
                row < 0
                || col < 0
                || row >= rows
                || col >= cols
                || board[row][col] != word[index]
            ) {
                return false
            }

            val temp = board[row][col]
            board[row][col] = '#'

            val found = dfs(row + 1, col, index + 1)
                || dfs(row - 1, col, index + 1)
                || dfs(row, col + 1, index + 1)
                || dfs(row, col - 1, index + 1)

            board[row][col] = temp
            return found
        }

        for (row in 0 until rows) {
            for (col in 0 until cols) {
                if (dfs(row, col, 0)) {
                    return true
                }
            }
        }

        return false
    }
}
