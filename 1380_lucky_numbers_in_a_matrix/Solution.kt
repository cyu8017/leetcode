// LeetCode 1380 - Lucky Numbers in a Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution {
    fun luckyNumbers(matrix: Array<IntArray>): List<Int> {
        val mins = matrix.map { row -> row.minOrNull()!! }.toSet()
        val cols = matrix[0].indices
        val maxs = cols.map { c -> matrix.maxOf { row -> row[c] } }.toSet()
        return mins.intersect(maxs).toList()
    }
}
