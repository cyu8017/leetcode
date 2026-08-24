// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

impl Solution {
    pub fn count_k_subsequences_with_max_beauty(s: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let mut vals: Vec<i32> = freq.into_iter().filter(|&f| f > 0).collect();
        if vals.len() < k as usize {
            return 0;
        }
        vals.sort_unstable_by(|a, b| b.cmp(a));
        let threshold = vals[k as usize - 1];
        let mut need = 0i32;
        let mut avail = 0i32;
        let mut prod = 1i64;
        for v in vals {
            if v > threshold {
                prod = prod * v as i64 % MOD;
                need += 1;
            } else if v == threshold {
                avail += 1;
            }
        }
        let remain = k - need;
        fn mod_pow(mut a: i64, mut b: i64) -> i64 {
            const MOD: i64 = 1_000_000_007;
            let mut res = 1i64;
            a %= MOD;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                b >>= 1;
            }
            res
        }
        fn comb(n: i32, r: i32) -> i64 {
            const MOD: i64 = 1_000_000_007;
            if r < 0 || r > n {
                return 0;
            }
            let mut num = 1i64;
            let mut den = 1i64;
            for i in 0..r {
                num = num * (n - i) as i64 % MOD;
                den = den * (i + 1) as i64 % MOD;
            }
            num * mod_pow(den, MOD - 2) % MOD
        }
        prod = prod * comb(avail, remain) % MOD;
        for _ in 0..remain {
            prod = prod * threshold as i64 % MOD;
        }
        prod as i32
    }
}
