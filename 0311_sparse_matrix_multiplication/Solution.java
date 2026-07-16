// LeetCode 0311 - Sparse Matrix Multiplication

// https://leetcode.com/problems/sparse-matrix-multiplication/



class Solution {

    public int[][] multiply(int[][] mat1, int[][] mat2) {

        int rows = mat1.length;

        int inner = mat1[0].length;

        int cols = mat2[0].length;

        int[][] result = new int[rows][cols];

        for (int row = 0; row < rows; row++) {

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

