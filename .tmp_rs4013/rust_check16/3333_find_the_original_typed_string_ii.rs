struct Solution;
// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

impl Solution {
    pub fn possible_string_count(word: String, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let w = word.as_bytes();
        let mut groups = Vec::new();
        let mut i = 0;
        while i < w.len() {
            let mut j = i;
            while j < w.len() && w[j] == w[i] {
                j += 1;
            }
            groups.push((j - i) as i32);
            i = j;
        }
        let mut total = 1i64;
        for &g in &groups {
            total = total * g as i64 % MOD;
        }
        if k as usize <= groups.len() {
            return total as i32;
        }
        let need = (k - 1) as usize;
        let mut dp = vec![0i32; need];
        dp[0] = 1;
        for &g in &groups {
            let mut ndp = vec![0i32; need];
            let mut pref = vec![0i32; need + 1];
            for i in 0..need {
                pref[i + 1] = (pref[i] as i64 + dp[i] as i64).rem_euclid(MOD) as i32;
            }
            for s in 0..need {
                let mut lo = s as i32 - g;
                if lo < 0 {
                    lo = 0;
                }
                let hi = s as i32 - 1;
                if hi >= 0 {
                    ndp[s] = (pref[hi as usize + 1] as i64 - pref[lo as usize] as i64 + MOD).rem_euclid(MOD) as i32;
                }
            }
            dp = ndp;
        }
        let mut bad = 0i64;
        for v in dp {
            bad = (bad + v as i64) % MOD;
        }
        ((total - bad + MOD) % MOD) as i32
    }
}

fn main() {}
