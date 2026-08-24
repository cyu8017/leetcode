// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

impl Solution {
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let k = k as usize;
        let mut dp = vec![0i64; k + 1];
        dp[0] = 1;
        for size in 1..=n {
            let mut nxt = vec![0i64; k + 1];
            let mut prefix = 0i64;
            for pairs in 0..=k {
                prefix = (prefix + dp[pairs]) % MOD;
                if pairs as i32 >= size {
                    prefix = (prefix - dp[pairs - size as usize] + MOD) % MOD;
                }
                nxt[pairs] = prefix;
            }
            dp = nxt;
        }
        dp[k] as i32
    }
}
