// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

impl Solution {
    pub fn count_palindromic_subsequences(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let s = s.as_bytes();
        let n = s.len();
        let mut dp = vec![vec![0i64; n]; n];
        for i in 0..n {
            dp[i][i] = 1;
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                if s[i] != s[j] {
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1];
                } else {
                    let mut left = i + 1;
                    let mut right = j - 1;
                    while left <= right && s[left] != s[i] {
                        left += 1;
                    }
                    while left <= right && s[right] != s[i] {
                        right -= 1;
                    }
                    if left > right {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2;
                    } else if left == right {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1];
                    }
                }
                dp[i][j] = (dp[i][j] % MOD + MOD) % MOD;
            }
        }
        dp[0][n - 1] as i32
    }
}
