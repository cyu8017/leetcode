// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution {
    fun checkValid(matrix: Array<IntArray>): Boolean {
        var n: Int = matrix.size
        for (i in 0 until n) {
            var row: BooleanArray = BooleanArray(n + 1), col = BooleanArray(n + 1)
            for (j in 0 until n) {
                if (row[matrix[i][j]] || col[matrix[j][i]]) return false
                row[matrix[i][j]] = col[matrix[j][i]] = true
            }
        }
        return true
    }
}
