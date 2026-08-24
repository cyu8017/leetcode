// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

impl Solution {
    pub fn unique_paths(grid: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        if grid[0][0] == 1 {
            return 0;
        }
        let mut dp = vec![vec![0; n]; m];
        dp[0][0] = 1;
        let next_cell = |i: i32, j: i32, mut di: i32, mut dj: i32| -> Option<(usize, usize)> {
            let mut ni = i + di;
            let mut nj = j + dj;
            while ni >= 0 && nj >= 0 && ni < m as i32 && nj < n as i32 && grid[ni as usize][nj as usize] == 1 {
                if dj == 1 {
                    di = 1;
                    dj = 0;
                } else {
                    di = 0;
                    dj = 1;
                }
                ni += di;
                nj += dj;
            }
            if ni < 0 || nj < 0 || ni >= m as i32 || nj >= n as i32 {
                None
            } else {
                Some((ni as usize, nj as usize))
            }
        };
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 || dp[i][j] == 0 {
                    continue;
                }
                if let Some((ni, nj)) = next_cell(i as i32, j as i32, 0, 1) {
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD;
                }
                if let Some((ni, nj)) = next_cell(i as i32, j as i32, 1, 0) {
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD;
                }
            }
        }
        dp[m - 1][n - 1]
    }
}
