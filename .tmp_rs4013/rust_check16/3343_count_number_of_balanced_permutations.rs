struct Solution;
// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

use std::collections::HashMap;

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

    pub fn count_balanced_permutations(num: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = [0i32; 10];
        let mut sum = 0;
        for c in num.bytes() {
            cnt[(c - b'0') as usize] += 1;
            sum += (c - b'0') as i32;
        }
        if sum % 2 == 1 {
            return 0;
        }
        let n = num.len();
        let half_n = n / 2;
        let half_s = sum / 2;
        let mut fact = vec![0i32; n + 1];
        let mut inv_f = vec![0i32; n + 1];
        fact[0] = 1;
        for i in 1..=n {
            fact[i] = (fact[i - 1] as i64 * i as i64 % MOD) as i32;
        }
        inv_f[n] = Self::mod_pow(fact[n] as i64, MOD - 2, MOD);
        for i in (1..=n).rev() {
            inv_f[i - 1] = (inv_f[i] as i64 * i as i64 % MOD) as i32;
        }
        let mut dp: HashMap<(i32, i32), i32> = HashMap::new();
        dp.insert((0, 0), 1);
        for d in 0..=9 {
            let mut ndp: HashMap<(i32, i32), i32> = HashMap::new();
            for (&(used, s), &ways) in &dp {
                for take in 0..=cnt[d] {
                    let nu = used + take;
                    let ns = s + take * d as i32;
                    if nu > half_n as i32 || ns > half_s {
                        continue;
                    }
                    let w = (ways as i64 * inv_f[take as usize] as i64 % MOD
                        * inv_f[(cnt[d] - take) as usize] as i64 % MOD) as i32;
                    *ndp.entry((nu, ns)).or_insert(0) = ((*ndp.get(&(nu, ns)).unwrap_or(&0) as i64 + w as i64) % MOD) as i32;
                }
            }
            dp = ndp;
        }
        let mut ans = *dp.get(&(half_n as i32, half_s)).unwrap_or(&0);
        ans = (ans as i64 * fact[half_n] as i64 % MOD * fact[n - half_n] as i64 % MOD) as i32;
        for d in 0..=9 {
            ans = (ans as i64 * fact[cnt[d] as usize] as i64 % MOD) as i32;
        }
        ans
    }
}

fn main() {}
