// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

impl Solution {
    pub fn minimum_operations(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = 0;
        for j in 0..n {
            for i in 1..m {
                if grid[i][j] <= grid[i - 1][j] {
                    let need = grid[i - 1][j] + 1;
                    ans += need - grid[i][j];
                    grid[i][j] = need;
                }
            }
        }
        ans
    }
}
