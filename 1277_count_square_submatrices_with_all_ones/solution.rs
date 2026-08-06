// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

impl Solution {
    pub fn count_squares(mut matrix: Vec<Vec<i32>>) -> i32 {
        let mut answer = 0;
        for r in 0..matrix.len() {
            for c in 0..matrix[0].len() {
                if matrix[r][c] > 0 && r > 0 && c > 0 {
                    matrix[r][c] += matrix[r - 1][c]
                        .min(matrix[r][c - 1])
                        .min(matrix[r - 1][c - 1]);
                }
                answer += matrix[r][c];
            }
        }
        answer
    }
}
