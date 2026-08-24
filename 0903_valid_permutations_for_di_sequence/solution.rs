// LeetCode 0903 - Valid Permutations for DI Sequence
// https://leetcode.com/problems/valid-permutations-for-di-sequence/

impl Solution {
    pub fn num_perms_di_sequence(s: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = s.len();
        let bytes = s.as_bytes();
        let mut dp = vec![1i32; n + 1];
        for i in 1..=n {
            let mut new_dp = vec![0i32; n + 1];
            if bytes[i - 1] == b'I' {
                let mut postfix = 0;
                for j in (0..=n - i).rev() {
                    postfix = (postfix + dp[j + 1]) % MOD;
                    new_dp[j] = postfix;
                }
            } else {
                let mut prefix = 0;
                for j in 0..=n - i {
                    prefix = (prefix + dp[j]) % MOD;
                    new_dp[j] = prefix;
                }
            }
            dp = new_dp;
        }
        dp[0]
    }
}
