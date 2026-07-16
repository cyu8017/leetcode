// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

class Solution {
    fun solveSudoku(board: Array<CharArray>) {
        val rows = Array(9) { mutableSetOf<Char>() }
        val cols = Array(9) { mutableSetOf<Char>() }
        val boxes = Array(9) { mutableSetOf<Char>() }
        val empty = mutableListOf<Pair<Int, Int>>()

        for (r in 0 until 9) {
            for (c in 0 until 9) {
                val value = board[r][c]
                if (value == '.') {
                    empty.add(r to c)
                    continue
                }
                val box = (r / 3) * 3 + c / 3
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
            }
        }

        fun backtrack(index: Int): Boolean {
            if (index == empty.size) {
                return true
            }

            val (r, c) = empty[index]
            val box = (r / 3) * 3 + c / 3
            for (digit in '1'..'9') {
                if (digit in rows[r] || digit in cols[c] || digit in boxes[box]) {
                    continue
                }

                board[r][c] = digit
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

                if (backtrack(index + 1)) {
                    return true
                }

                board[r][c] = '.'
                rows[r].remove(digit)
                cols[c].remove(digit)
                boxes[box].remove(digit)
            }

            return false
        }

        backtrack(0)
    }
}
