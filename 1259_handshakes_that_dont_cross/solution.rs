// LeetCode 1259 - Handshakes That Don't Cross
// https://leetcode.com/problems/handshakes-that-dont-cross/

impl Solution {
    pub fn number_of_ways(num_people: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = num_people as usize;
        let mut dp = vec![0i64; n + 1];
        dp[0] = 1;
        let mut people = 2;
        while people <= n {
            let mut sum = 0i64;
            let mut left = 0;
            while left < people {
                sum = (sum + dp[left] * dp[people - 2 - left]) % MOD;
                left += 2;
            }
            dp[people] = sum;
            people += 2;
        }
        dp[n] as i32
    }
}
