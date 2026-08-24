// LeetCode 2266 - Count Number of Texts
// https://leetcode.com/problems/count-number-of-texts/

impl Solution {
    pub fn count_texts(pressed_keys: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let s = pressed_keys.as_bytes();
        let n = s.len();
        let mut dp = vec![0i32; n + 1];
        dp[0] = 1;
        for i in 1..=n {
            dp[i] = dp[i - 1];
            let max_press = if s[i - 1] == b'7' || s[i - 1] == b'9' { 4 } else { 3 };
            for j in 2..=max_press {
                if j > i {
                    break;
                }
                if s[i - j] != s[i - 1] {
                    break;
                }
                dp[i] = (dp[i] + dp[i - j]) % MOD;
            }
        }
        dp[n]
    }
}
