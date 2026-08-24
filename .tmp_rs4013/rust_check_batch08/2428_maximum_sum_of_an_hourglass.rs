struct Solution;
// LeetCode 2428 - Maximum Sum of an Hourglass
// https://leetcode.com/problems/maximum-sum-of-an-hourglass/

impl Solution {
    pub fn max_sum(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;
        for i in 0..m.saturating_sub(2) {
            for j in 0..n.saturating_sub(2) {
                let s = grid[i][j]
                    + grid[i][j + 1]
                    + grid[i][j + 2]
                    + grid[i + 1][j + 1]
                    + grid[i + 2][j]
                    + grid[i + 2][j + 1]
                    + grid[i + 2][j + 2];
                ans = ans.max(s);
            }
        }
        ans
    }
}

fn main() {}
