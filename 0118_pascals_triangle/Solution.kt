// LeetCode 0118 - Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/

class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        val triangle = mutableListOf<List<Int>>()
        for (row in 0 until numRows) {
            val values = MutableList(row + 1) { 1 }
            for (col in 1 until row) {
                values[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
            }
            triangle.add(values)
        }
        return triangle
    }
}