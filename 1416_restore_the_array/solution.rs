// LeetCode 1416 - Restore The Array
// https://leetcode.com/problems/restore-the-array/

impl Solution {
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let s = s.as_bytes();
        let n = s.len();
        let k = k as i64;
        let mut dp = vec![0i64; n + 1];
        dp[n] = 1;
        for i in (0..n).rev() {
            if s[i] == b'0' {
                continue;
            }
            let mut value = 0i64;
            for j in i..n {
                value = value * 10 + (s[j] - b'0') as i64;
                if value > k {
                    break;
                }
                dp[i] = (dp[i] + dp[j + 1]) % MOD;
            }
        }
        dp[0] as i32
    }
}
