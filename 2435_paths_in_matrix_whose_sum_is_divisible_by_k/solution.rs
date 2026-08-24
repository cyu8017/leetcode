// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

impl Solution {
    pub fn number_of_paths(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        let k = k as usize;
        let mut dp = vec![vec![vec![0; k]; n]; m];
        dp[0][0][(grid[0][0] as usize) % k] = 1;
        for i in 0..m {
            for j in 0..n {
                for r in 0..k {
                    if dp[i][j][r] == 0 {
                        continue;
                    }
                    if i + 1 < m {
                        let nr = (r + grid[i + 1][j] as usize) % k;
                        dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % MOD;
                    }
                    if j + 1 < n {
                        let nr = (r + grid[i][j + 1] as usize) % k;
                        dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % MOD;
                    }
                }
            }
        }
        dp[m - 1][n - 1][0]
    }
}
