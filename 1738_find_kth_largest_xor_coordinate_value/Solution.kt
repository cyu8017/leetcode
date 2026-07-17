// LeetCode 1738 - Find Kth Largest XOR Coordinate Value
// https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

class Solution {
    fun kthLargestValue(matrix: Array<IntArray>, k: Int): Int {
        val rows = matrix.size
        val cols = matrix[0].size
        val pref = Array(rows + 1) { IntArray(cols + 1) }
        val values = IntArray(rows * cols)
        var index = 0
        for (r in 1..rows) {
            for (c in 1..cols) {
                pref[r][c] = pref[r - 1][c] xor pref[r][c - 1] xor pref[r - 1][c - 1] xor matrix[r - 1][c - 1]
                values[index++] = pref[r][c]
            }
        }
        values.sort()
        return values[values.size - k]
    }
}
