// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution {
    fun restoreMatrix(rowSum: IntArray, colSum: IntArray): Array<IntArray> {
        val ans = Array(rowSum.size) { IntArray(colSum.size) }
        var i = 0
        var j = 0
        while (i < rowSum.size && j < colSum.size) {
            val x = minOf(rowSum[i], colSum[j])
            ans[i][j] = x
            rowSum[i] -= x
            colSum[j] -= x
            if (rowSum[i] == 0) i++
            if (colSum[j] == 0) j++
        }
        return ans
    }
}
