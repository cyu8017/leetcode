// LeetCode 0073 - Set Matrix Zeroes
// https://leetcode.com/problems/set-matrix-zeroes/

impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let rows = matrix.len();
        let cols = matrix[0].len();
        let first_row_zero = matrix[0].iter().any(|&v| v == 0);
        let first_col_zero = matrix.iter().any(|row| row[0] == 0);

        for i in 1..rows {
            for j in 1..cols {
                if matrix[i][j] == 0 {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for i in 1..rows {
            for j in 1..cols {
                if matrix[i][0] == 0 || matrix[0][j] == 0 {
                    matrix[i][j] = 0;
                }
            }
        }

        if first_row_zero {
            for j in 0..cols {
                matrix[0][j] = 0;
            }
        }
        if first_col_zero {
            for i in 0..rows {
                matrix[i][0] = 0;
            }
        }
    }
}
