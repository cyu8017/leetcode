struct Solution;
// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let high = high as usize;
        let low = low as usize;
        let zero = zero as usize;
        let one = one as usize;
        let mut dp = vec![0; high + 1];
        dp[0] = 1;
        let mut ans = 0;
        for i in 1..=high {
            if i >= zero {
                dp[i] = (dp[i] + dp[i - zero]) % MOD;
            }
            if i >= one {
                dp[i] = (dp[i] + dp[i - one]) % MOD;
            }
            if i >= low {
                ans = (ans + dp[i]) % MOD;
            }
        }
        ans
    }
}

fn main() {}
