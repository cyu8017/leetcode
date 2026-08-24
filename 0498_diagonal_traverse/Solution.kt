// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

class Solution {
    fun findDiagonalOrder(mat: Array<IntArray>): IntArray {
        if (mat.isEmpty() || mat[0].isEmpty()) return intArrayOf()
        val rows = mat.size
        val cols = mat[0].size
        val result = IntArray(rows * cols)
        var row = 0
        var col = 0
        var upward = true
        var index = 0

        while (index < rows * cols) {
            result[index++] = mat[row][col]
            if (upward) {
                when {
                    col == cols - 1 -> {
                        row++
                        upward = false
                    }
                    row == 0 -> {
                        col++
                        upward = false
                    }
                    else -> {
                        row--
                        col++
                    }
                }
            } else {
                when {
                    row == rows - 1 -> {
                        col++
                        upward = true
                    }
                    col == 0 -> {
                        row++
                        upward = true
                    }
                    else -> {
                        row++
                        col--
                    }
                }
            }
        }
        return result
    }
}
