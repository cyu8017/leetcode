// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

impl Solution {
    pub fn number_of_ways(n: i32, x: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = n as i64;
        let mut powers = Vec::new();
        let mut i = 1i64;
        loop {
            let mut p = 1i64;
            for _ in 0..x {
                p *= i;
                if p > n {
                    break;
                }
            }
            if p > n {
                break;
            }
            powers.push(p as i32);
            i += 1;
        }
        let n = n as usize;
        let mut dp = vec![0i32; n + 1];
        dp[0] = 1;
        for p in powers {
            let p = p as usize;
            for s in (p..=n).rev() {
                dp[s] = (dp[s] + dp[s - p]) % MOD;
            }
        }
        dp[n]
    }
}
