// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

impl Solution {
    pub fn max_moves(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![0; m];
        for c in (0..n - 1).rev() {
            let mut ndp = vec![0; m];
            for r in 0..m {
                let mut best = 0;
                for dr in [-1i32, 0, 1] {
                    let nr = r as i32 + dr;
                    if nr >= 0
                        && (nr as usize) < m
                        && grid[nr as usize][c + 1] > grid[r][c]
                    {
                        best = best.max(1 + dp[nr as usize]);
                    }
                }
                ndp[r] = best;
            }
            dp = ndp;
        }
        *dp.iter().max().unwrap()
    }
}
