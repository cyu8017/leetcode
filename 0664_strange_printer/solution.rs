// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

impl Solution {
    pub fn strange_printer(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        if n == 0 {
            return 0;
        }
        let mut dp = vec![vec![0i32; n]; n];
        for i in (0..n).rev() {
            dp[i][i] = 1;
            for j in i + 1..n {
                dp[i][j] = dp[i + 1][j] + 1;
                for k in i + 1..=j {
                    if s[k] == s[i] {
                        let extra = if k + 1 <= j { dp[k + 1][j] } else { 0 };
                        dp[i][j] = dp[i][j].min(dp[i][k - 1] + extra);
                    }
                }
            }
        }
        dp[0][n - 1]
    }
}
