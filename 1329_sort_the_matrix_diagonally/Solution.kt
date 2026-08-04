// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution {
    fun diagonalSort(mat: Array<IntArray>): Array<IntArray> {
        val diagonals = mutableMapOf<Int, MutableList<Int>>()
        for (r in mat.indices) {
            for (c in mat[r].indices) {
                diagonals.getOrPut(r - c) { mutableListOf() }.add(mat[r][c])
            }
        }
        for (values in diagonals.values) values.sortDescending()
        for (r in mat.indices) {
            for (c in mat[r].indices) {
                mat[r][c] = diagonals[r - c]!!.removeAt(diagonals[r - c]!!.lastIndex)
            }
        }
        return mat
    }
}
