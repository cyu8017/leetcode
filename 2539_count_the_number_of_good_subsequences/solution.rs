// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

impl Solution {
    pub fn count_good_subsequences(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut e: i64) -> i64 {
            let mut res = 1i64;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res
        }
        let mut cnt = [0i32; 26];
        let mut maxf = 0;
        for c in s.bytes() {
            let i = (c - b'a') as usize;
            cnt[i] += 1;
            if cnt[i] > maxf {
                maxf = cnt[i];
            }
        }
        let maxf = maxf as usize;
        let mut fact = vec![0i64; maxf + 1];
        let mut inv_fact = vec![0i64; maxf + 1];
        fact[0] = 1;
        for i in 1..=maxf {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        inv_fact[maxf] = mod_pow(fact[maxf], MOD - 2);
        for i in (1..=maxf).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }
        let comb = |n: i32, k: i32| -> i64 {
            if k < 0 || k > n {
                return 0;
            }
            let n = n as usize;
            let k = k as usize;
            fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        };
        let mut ans = 0i64;
        for k in 1..=maxf as i32 {
            let mut ways = 1i64;
            for i in 0..26 {
                if cnt[i] >= k {
                    ways = ways * (1 + comb(cnt[i], k)) % MOD;
                }
            }
            ans = (ans + ways - 1 + MOD) % MOD;
        }
        ans as i32
    }
}
