struct Solution;
// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

impl Solution {
    pub fn count_paths_with_xor_value(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![vec![vec![0; 16]; n]; m];
        dp[0][0][grid[0][0] as usize] = 1;
        for i in 0..m {
            for j in 0..n {
                for x in 0..16 {
                    if dp[i][j][x] == 0 {
                        continue;
                    }
                    if i + 1 < m {
                        let nx = x ^ grid[i + 1][j] as usize;
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % MOD;
                    }
                    if j + 1 < n {
                        let nx = x ^ grid[i][j + 1] as usize;
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % MOD;
                    }
                }
            }
        }
        dp[m - 1][n - 1][k as usize]
    }
}

fn main() {}
