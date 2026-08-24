struct Solution;
// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut row = vec![0; m];
        let mut col = vec![0; n];
        for i in 0..m {
            for j in 0..n {
                row[i] += grid[i][j];
                col[j] += grid[i][j];
            }
        }
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                ans[i][j] = row[i] + col[j] - (m as i32 - row[i]) - (n as i32 - col[j]);
            }
        }
        ans
    }
}

fn main() {}
