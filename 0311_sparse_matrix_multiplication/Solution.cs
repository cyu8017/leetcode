// LeetCode 0311 - Sparse Matrix Multiplication

// https://leetcode.com/problems/sparse-matrix-multiplication/



public class Solution {

    public int[][] Multiply(int[][] mat1, int[][] mat2) {

        int rows = mat1.Length;

        int inner = mat1[0].Length;

        int cols = mat2[0].Length;

        int[][] result = new int[rows][];

        for (int row = 0; row < rows; row++) {

            result[row] = new int[cols];

            for (int index = 0; index < inner; index++) {

                if (mat1[row][index] == 0) {

                    continue;

                }

                for (int col = 0; col < cols; col++) {

                    if (mat2[index][col] != 0) {

                        result[row][col] += mat1[row][index] * mat2[index][col];

                    }

                }

            }

        }

        return result;

    }

}

