// LeetCode 0311 - Sparse Matrix Multiplication

// https://leetcode.com/problems/sparse-matrix-multiplication/



class Solution {

    fun multiply(mat1: Array<IntArray>, mat2: Array<IntArray>): Array<IntArray> {

        val rows = mat1.size

        val inner = mat1[0].size

        val cols = mat2[0].size

        val result = Array(rows) { IntArray(cols) }

        for (row in 0 until rows) {

            for (index in 0 until inner) {

                if (mat1[row][index] == 0) {

                    continue

                }

                for (col in 0 until cols) {

                    if (mat2[index][col] != 0) {

                        result[row][col] += mat1[row][index] * mat2[index][col]

                    }

                }

            }

        }

        return result

    }

}

