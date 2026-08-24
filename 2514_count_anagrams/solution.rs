// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

impl Solution {
    pub fn count_anagrams(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn mod_pow(mut a: i64, mut e: i64) -> i64 {
            let mut res = 1;
            a %= MOD;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res
        }
        let words: Vec<&str> = s.split_whitespace().collect();
        let max_n = words.iter().map(|w| w.len()).max().unwrap_or(0);
        let mut fact = vec![1i64; max_n + 1];
        let mut inv_fact = vec![1i64; max_n + 1];
        for i in 1..=max_n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        inv_fact[max_n] = mod_pow(fact[max_n], MOD - 2);
        for i in (1..=max_n).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }
        let mut ans = 1i64;
        for word in words {
            let mut cnt = [0usize; 26];
            for c in word.bytes() {
                cnt[(c - b'a') as usize] += 1;
            }
            let mut cur = fact[word.len()];
            for c in cnt {
                cur = cur * inv_fact[c] % MOD;
            }
            ans = ans * cur % MOD;
        }
        ans as i32
    }
}
