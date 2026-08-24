// LeetCode 2304 - Minimum Path Cost in a Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/

impl Solution {
    pub fn min_path_cost(grid: Vec<Vec<i32>>, move_cost: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = grid[0].clone();
        for r in 0..m - 1 {
            let mut next = vec![i32::MAX / 2; n];
            for c in 0..n {
                let from = grid[r][c] as usize;
                for nc in 0..n {
                    next[nc] = next[nc].min(dp[c] + move_cost[from][nc] + grid[r + 1][nc]);
                }
            }
            dp = next;
        }
        *dp.iter().min().unwrap()
    }
}
