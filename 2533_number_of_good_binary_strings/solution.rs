// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

impl Solution {
    pub fn good_binary_strings(min_length: i32, max_length: i32, one_group: i32, zero_group: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let max_length = max_length as usize;
        let min_length = min_length as usize;
        let one_group = one_group as usize;
        let zero_group = zero_group as usize;
        let mut dp = vec![0i32; max_length + 1];
        dp[0] = 1;
        for i in 0..=max_length {
            if dp[i] == 0 {
                continue;
            }
            if i + one_group <= max_length {
                dp[i + one_group] = (dp[i + one_group] + dp[i]) % MOD;
            }
            if i + zero_group <= max_length {
                dp[i + zero_group] = (dp[i + zero_group] + dp[i]) % MOD;
            }
        }
        let mut ans = 0i32;
        for i in min_length..=max_length {
            ans = (ans + dp[i]) % MOD;
        }
        ans
    }
}
