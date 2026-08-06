// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

impl Solution {
    pub fn num_ways(steps: i32, arr_len: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let width = arr_len.min(steps / 2 + 1) as usize;
        let mut dp = vec![0; width];
        dp[0] = 1;
        for _ in 0..steps {
            let mut nxt = vec![0; width];
            for i in 0..width {
                nxt[i] = dp[i];
                if i > 0 {
                    nxt[i] = (nxt[i] + dp[i - 1]) % MOD;
                }
                if i + 1 < width {
                    nxt[i] = (nxt[i] + dp[i + 1]) % MOD;
                }
            }
            dp = nxt;
        }
        dp[0]
    }
}
