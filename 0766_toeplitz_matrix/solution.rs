// LeetCode 0766 - Toeplitz Matrix
// https://leetcode.com/problems/toeplitz-matrix/

impl Solution {
    pub fn is_toeplitz_matrix(matrix: Vec<Vec<i32>>) -> bool {
        for r in 1..matrix.len() {
            for c in 1..matrix[0].len() {
                if matrix[r][c] != matrix[r - 1][c - 1] {
                    return false;
                }
            }
        }
        true
    }
}
