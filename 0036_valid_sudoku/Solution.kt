// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        val rows = Array(9) { mutableSetOf<Char>() }
        val cols = Array(9) { mutableSetOf<Char>() }
        val boxes = Array(9) { mutableSetOf<Char>() }

        for (r in 0 until 9) {
            for (c in 0 until 9) {
                val value = board[r][c]
                if (value == '.') {
                    continue
                }

                val box = (r / 3) * 3 + c / 3
                if (value in rows[r] || value in cols[c] || value in boxes[box]) {
                    return false
                }

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
            }
        }

        return true
    }
}
