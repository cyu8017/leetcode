// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

class Solution {
    fun modifiedMatrix(matrix: Array<IntArray>): Array<IntArray> {
        var m = matrix.size
        var n = matrix[0].size
        for (j in 0 until n) {
            var mx = -1
            for (i in 0 until m) { mx = maxOf(mx, matrix[i][j]) }
            for (i in 0 until m) { if (matrix[i][j] == -1) matrix[i][j] = mx }
        }
        return matrix
    }
}
