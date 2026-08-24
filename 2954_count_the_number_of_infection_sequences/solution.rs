// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

impl Solution {
    pub fn number_of_sequence(n: i32, sick: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let mut fact = vec![0i64; n + 1];
        let mut inv_fact = vec![0i64; n + 1];
        fact[0] = 1;
        for i in 1..=n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        fn mod_pow(mut a: i64, mut b: i32) -> i64 {
            const MOD: i64 = 1_000_000_007;
            let mut res = 1i64;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            res
        }
        inv_fact[n] = mod_pow(fact[n], 1_000_000_005);
        for i in (1..=n).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }
        let m = sick.len();
        let total_empty = n - m;
        let mut ans = fact[total_empty];
        let mut prev = -1i32;
        for &s in &sick {
            let gap = (s - prev - 1) as usize;
            if prev == -1 {
                ans = ans * inv_fact[gap] % MOD;
            } else if gap > 0 {
                ans = ans * inv_fact[gap] % MOD * mod_pow(2, gap as i32 - 1) % MOD;
            }
            prev = s;
        }
        let gap = (n as i32 - prev - 1) as usize;
        ans = ans * inv_fact[gap] % MOD;
        ans as i32
    }
}
