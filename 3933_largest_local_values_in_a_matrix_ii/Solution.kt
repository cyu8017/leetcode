// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

class Solution {
    fun countLocalMaximums(matrix: Array<IntArray>): Int {
        val rows = matrix.size
        val cols = matrix[0].size
        val positions = Array(201) { ArrayList<IntArray>() }
        for (row in 0 until rows) {
            for (col in 0 until cols) {
                val value = matrix[row][col]
                if (value > 0) positions[value].add(intArrayOf(row, col))
            }
        }
        var answer = 0
        for (value in 1..200) {
            if (positions[value].isEmpty()) continue
            val prefix = Array(rows + 1) { IntArray(cols + 1) }
            for (row in 0 until rows) {
                for (col in 0 until cols) {
                    val add = if (matrix[row][col] > value) 1 else 0
                    prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add
                }
            }
            for (pos in positions[value]) {
                val row = pos[0]
                val col = pos[1]
                val top = maxOf(0, row - value)
                val bottom = minOf(rows - 1, row + value)
                val left = maxOf(0, col - value)
                val right = minOf(cols - 1, col + value)
                var greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left]
                for (dr in intArrayOf(-value, value)) {
                    for (dc in intArrayOf(-value, value)) {
                        val rr = row + dr
                        val cc = col + dc
                        if (rr >= 0 && rr < rows && cc >= 0 && cc < cols && matrix[rr][cc] > value) greater--
                    }
                }
                if (greater == 0) answer++
            }
        }
        return answer
    }
}
