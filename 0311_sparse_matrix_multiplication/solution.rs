// LeetCode 0311 - Sparse Matrix Multiplication
// https://leetcode.com/problems/sparse-matrix-multiplication/

impl Solution {
    pub fn multiply(mat1: Vec<Vec<i32>>, mat2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = mat1.len();
        let inner = mat1[0].len();
        let cols = mat2[0].len();
        let mut result = vec![vec![0; cols]; rows];

        for row in 0..rows {
            for index in 0..inner {
                if mat1[row][index] == 0 {
                    continue;
                }
                for col in 0..cols {
                    if mat2[index][col] != 0 {
                        result[row][col] += mat1[row][index] * mat2[index][col];
                    }
                }
            }
        }

        result
    }
}
