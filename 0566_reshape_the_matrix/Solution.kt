// LeetCode 0566 - Reshape the Matrix
// https://leetcode.com/problems/reshape-the-matrix/


class Solution {
    fun matrixReshape(mat: Array<IntArray>, r: Int, c: Int): Array<IntArray> {
        val rows = mat.size
        val cols = mat[0].size
        if (rows * cols != r * c) return mat
        val result = Array(r) { IntArray(c) }
        var index = 0
        for (i in 0 until r) {
            for (j in 0 until c) {
                result[i][j] = mat[index / cols][index % cols]
                index++
            }
        }
        return result
    }
}
