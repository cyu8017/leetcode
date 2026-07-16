// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

import java.util.ArrayDeque

class Solution {
    fun updateMatrix(mat: Array<IntArray>): Array<IntArray> {
        val rows = mat.size
        val cols = mat[0].size
        val dist = Array(rows) { IntArray(cols) { 1_000_000_000 } }
        val queue = ArrayDeque<IntArray>()

        for (row in 0 until rows) {
            for (col in 0 until cols) {
                if (mat[row][col] == 0) {
                    dist[row][col] = 0
                    queue.add(intArrayOf(row, col))
                }
            }
        }

        val directions = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (queue.isNotEmpty()) {
            val cell = queue.removeFirst()
            val row = cell[0]
            val col = cell[1]
            for (direction in directions) {
                val nr = row + direction[0]
                val nc = col + direction[1]
                if (nr in 0 until rows && nc in 0 until cols && dist[nr][nc] > dist[row][col] + 1) {
                    dist[nr][nc] = dist[row][col] + 1
                    queue.add(intArrayOf(nr, nc))
                }
            }
        }

        return dist
    }
}
