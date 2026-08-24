struct Solution;
// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

impl Solution {
    pub fn max_coins(lane1: Vec<i32>, lane2: Vec<i32>) -> i64 {
        let n = lane1.len();
        const NEG: i64 = -(1i64 << 60);
        let mut dp = [[0i64; 2]; 2];
        dp[0][0] = lane1[0] as i64;
        dp[1][0] = lane2[0] as i64;
        dp[0][1] = NEG;
        dp[1][1] = NEG;
        let mut ans = dp[0][0].max(dp[1][0]);
        for i in 1..n {
            let mut ndp = [[0i64; 2]; 2];
            ndp[0][0] = dp[0][0].max(0) + lane1[i] as i64;
            ndp[1][0] = dp[1][0].max(0) + lane2[i] as i64;
            ndp[0][1] = dp[0][1].max(dp[1][0]) + lane1[i] as i64;
            ndp[1][1] = dp[1][1].max(dp[0][0]) + lane2[i] as i64;
            if lane1[i] as i64 > ndp[0][0] {
                ndp[0][0] = lane1[i] as i64;
            }
            if lane2[i] as i64 > ndp[1][0] {
                ndp[1][0] = lane2[i] as i64;
            }
            for a in 0..2 {
                for b in 0..2 {
                    dp[a][b] = ndp[a][b];
                    if dp[a][b] > ans {
                        ans = dp[a][b];
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
