// LeetCode 1476 - Subrectangle Queries
// https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries(private val rectangle: Array<IntArray>) {
    fun updateSubrectangle(row1: Int, col1: Int, row2: Int, col2: Int, newValue: Int) {
        for (r in row1..row2) {
            for (c in col1..col2) {
                rectangle[r][c] = newValue
            }
        }
    }

    fun getValue(row: Int, col: Int): Int = rectangle[row][col]
}
