struct Solution;
// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

impl Solution {
    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32 {
        let m = coins.len();
        let n = coins[0].len();
        const NEG: i32 = -(1 << 30);
        let mut dp = vec![vec![vec![NEG; 3]; n]; m];
        if coins[0][0] < 0 {
            dp[0][0][0] = coins[0][0];
            dp[0][0][1] = 0;
            dp[0][0][2] = 0;
        } else {
            dp[0][0][0] = coins[0][0];
            dp[0][0][1] = coins[0][0];
            dp[0][0][2] = coins[0][0];
        }
        for i in 0..m {
            for j in 0..n {
                if i == 0 && j == 0 {
                    continue;
                }
                for k in 0..3 {
                    let mut best = NEG;
                    if i > 0 {
                        best = best.max(dp[i - 1][j][k]);
                    }
                    if j > 0 {
                        best = best.max(dp[i][j - 1][k]);
                    }
                    if best == NEG {
                        continue;
                    }
                    if coins[i][j] >= 0 {
                        dp[i][j][k] = best + coins[i][j];
                    } else {
                        dp[i][j][k] = dp[i][j][k].max(best + coins[i][j]);
                    }
                }
                for k in 1..3 {
                    let mut best = NEG;
                    if i > 0 {
                        best = best.max(dp[i - 1][j][k - 1]);
                    }
                    if j > 0 {
                        best = best.max(dp[i][j - 1][k - 1]);
                    }
                    if best != NEG && coins[i][j] < 0 {
                        dp[i][j][k] = dp[i][j][k].max(best);
                    }
                }
            }
        }
        dp[m - 1][n - 1][0]
            .max(dp[m - 1][n - 1][1])
            .max(dp[m - 1][n - 1][2])
    }
}

fn main() {}
