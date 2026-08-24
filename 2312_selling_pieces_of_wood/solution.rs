// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

impl Solution {
    pub fn selling_wood(m: i32, n: i32, prices: Vec<Vec<i32>>) -> i64 {
        let m = m as usize;
        let n = n as usize;
        let mut price = vec![vec![0i64; n + 1]; m + 1];
        let mut dp = vec![vec![0i64; n + 1]; m + 1];
        for p in prices {
            price[p[0] as usize][p[1] as usize] = p[2] as i64;
        }
        for h in 1..=m {
            for w in 1..=n {
                let mut best = price[h][w];
                for i in 1..h {
                    best = best.max(dp[i][w] + dp[h - i][w]);
                }
                for j in 1..w {
                    best = best.max(dp[h][j] + dp[h][w - j]);
                }
                dp[h][w] = best;
            }
        }
        dp[m][n]
    }
}
