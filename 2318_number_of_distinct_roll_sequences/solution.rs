// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

impl Solution {
    pub fn distinct_sequences(n: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let n = n as usize;
        let mut dp = vec![vec![vec![0i32; 7]; 7]; n + 1];
        for a in 1..=6 {
            dp[1][a][0] = 1;
        }
        for i in 2..=n {
            for prev in 1..=6 {
                for pprev in 0..=6 {
                    if dp[i - 1][prev][pprev] == 0 {
                        continue;
                    }
                    for cur in 1..=6 {
                        if cur == prev || cur == pprev || gcd(cur as i32, prev as i32) != 1 {
                            continue;
                        }
                        dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % MOD;
                    }
                }
            }
        }
        let mut ans = 0;
        for a in 1..=6 {
            for b in 0..=6 {
                ans = (ans + dp[n][a][b]) % MOD;
            }
        }
        ans
    }
}
