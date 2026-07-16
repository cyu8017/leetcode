// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

class Solution {
    fun solveNQueens(n: Int): List<List<String>> {
        val result = mutableListOf<List<String>>()
        val cols = HashSet<Int>()
        val diag1 = HashSet<Int>()
        val diag2 = HashSet<Int>()
        val board = Array(n) { ".".repeat(n) }

        fun backtrack(row: Int) {
            if (row == n) {
                result.add(board.toList())
                return
            }

            for (col in 0 until n) {
                if (col in cols || row + col in diag1 || row - col in diag2) {
                    continue
                }

                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                val rowChars = board[row].toCharArray()
                rowChars[col] = 'Q'
                board[row] = rowChars.concatToString()

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
                board[row] = ".".repeat(n)
            }
        }

        backtrack(0)
        return result
    }
}
