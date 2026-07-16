// LeetCode 0329 - Longest Increasing Path in a Matrix

// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/



class Solution {

    private lateinit var matrix: Array<IntArray>

    private lateinit var memo: Array<IntArray>



    private val directions = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))



    fun longestIncreasingPath(matrix: Array<IntArray>): Int {

        if (matrix.isEmpty() || matrix[0].isEmpty()) {

            return 0

        }

        this.matrix = matrix

        memo = Array(matrix.size) { IntArray(matrix[0].size) }

        var best = 0

        for (row in matrix.indices) {

            for (col in matrix[0].indices) {

                best = maxOf(best, dfs(row, col))

            }

        }

        return best

    }



    private fun dfs(row: Int, col: Int): Int {

        if (memo[row][col] != 0) {

            return memo[row][col]

        }

        var best = 1

        for ((dr, dc) in directions) {

            val nextRow = row + dr

            val nextCol = col + dc

            if (nextRow in matrix.indices && nextCol in matrix[0].indices

                && matrix[nextRow][nextCol] > matrix[row][col]

            ) {

                best = maxOf(best, 1 + dfs(nextRow, nextCol))

            }

        }

        memo[row][col] = best

        return best

    }

}

