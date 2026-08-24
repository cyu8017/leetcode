// LeetCode 0867 - Transpose Matrix
// https://leetcode.com/problems/transpose-matrix/

impl Solution {
    pub fn transpose(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut ans = vec![vec![0; m]; n];
        for i in 0..m {
            for j in 0..n {
                ans[j][i] = matrix[i][j];
            }
        }
        ans
    }
}
