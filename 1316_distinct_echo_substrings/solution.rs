// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

use std::collections::HashSet;

impl Solution {
    pub fn distinct_echo_substrings(text: String) -> i32 {
        let bytes = text.as_bytes();
        let n = bytes.len();
        const MOD1: i64 = 1_000_000_007;
        const MOD2: i64 = 1_000_000_009;
        const BASE: i64 = 911_382_323;
        let mut h1 = vec![0i64; n + 1];
        let mut h2 = vec![0i64; n + 1];
        let mut p1 = vec![1i64; n + 1];
        let mut p2 = vec![1i64; n + 1];
        for i in 0..n {
            let code = bytes[i] as i64;
            h1[i + 1] = (h1[i] * BASE + code) % MOD1;
            h2[i + 1] = (h2[i] * BASE + code) % MOD2;
            p1[i + 1] = p1[i] * BASE % MOD1;
            p2[i + 1] = p2[i] * BASE % MOD2;
        }
        let hashed = |left: usize, right: usize| -> (i64, i64) {
            let length = right - left;
            (
                (h1[right] - h1[left] * p1[length] % MOD1 + MOD1) % MOD1,
                (h2[right] - h2[left] * p2[length] % MOD2 + MOD2) % MOD2,
            )
        };
        let mut echoes = HashSet::new();
        for half in 1..=n / 2 {
            for left in 0..=n - 2 * half {
                if hashed(left, left + half) == hashed(left + half, left + 2 * half) {
                    let (a, b) = hashed(left, left + 2 * half);
                    echoes.insert((2 * half, a, b));
                }
            }
        }
        echoes.len() as i32
    }
}
