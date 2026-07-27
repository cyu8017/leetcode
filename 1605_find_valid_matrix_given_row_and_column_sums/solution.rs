// LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

impl Solution {
    pub fn restore_matrix(mut row_sum: Vec<i32>, mut col_sum: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans = vec![vec![0; col_sum.len()]; row_sum.len()];
        let (mut i, mut j) = (0usize, 0usize);
        while i < row_sum.len() && j < col_sum.len() {
            let x = row_sum[i].min(col_sum[j]);
            ans[i][j] = x;
            row_sum[i] -= x;
            col_sum[j] -= x;
            if row_sum[i] == 0 {
                i += 1;
            }
            if col_sum[j] == 0 {
                j += 1;
            }
        }
        ans
    }
}
