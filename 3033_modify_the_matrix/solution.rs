// LeetCode 3033 - Modify the Matrix
// https://leetcode.com/problems/modify-the-matrix/

impl Solution {
    pub fn modified_matrix(mut matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        let n = matrix[0].len();
        for j in 0..n {
            let mut mx = -1;
            for i in 0..m {
                mx = mx.max(matrix[i][j]);
            }
            for i in 0..m {
                if matrix[i][j] == -1 {
                    matrix[i][j] = mx;
                }
            }
        }
        matrix
    }
}
