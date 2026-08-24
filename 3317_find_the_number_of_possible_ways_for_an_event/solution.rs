// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

impl Solution {
    fn mod_pow(mut a: i64, mut e: i64, modulus: i64) -> i32 {
        let mut r = 1i64;
        a %= modulus;
        while e > 0 {
            if e & 1 == 1 {
                r = r * a % modulus;
            }
            a = a * a % modulus;
            e >>= 1;
        }
        r as i32
    }

    pub fn number_of_ways(n: i32, x: i32, y: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let x = x as usize;
        let mut dp = vec![vec![0i32; x + 1]; n + 1];
        dp[0][0] = 1;
        for i in 1..=n {
            for j in 1..=x.min(i) {
                dp[i][j] = ((dp[i - 1][j - 1] as i64 + j as i64 * dp[i - 1][j] as i64 % MOD) % MOD) as i32;
            }
        }
        let mut fact = vec![0i32; x + 1];
        fact[0] = 1;
        for i in 1..=x {
            fact[i] = (fact[i - 1] as i64 * i as i64 % MOD) as i32;
        }
        let mut ans = 0i32;
        let mut ypow = 1i32;
        for k in 1..=x.min(n) {
            ypow = (ypow as i64 * y as i64 % MOD) as i32;
            let perm = (fact[x] as i64 * Self::mod_pow(fact[x - k] as i64, MOD - 2, MOD) as i64 % MOD) as i32;
            ans = ((ans as i64 + dp[n][k] as i64 * perm as i64 % MOD * ypow as i64 % MOD) % MOD) as i32;
        }
        ans
    }
}
