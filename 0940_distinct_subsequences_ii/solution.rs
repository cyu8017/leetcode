// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

impl Solution {
    pub fn distinct_subseq_ii(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut ends = [0i64; 26];
        let mut total = 1i64;
        for ch in s.bytes() {
            let prev = ends[(ch - b'a') as usize];
            ends[(ch - b'a') as usize] = total;
            total = (total - prev + ends[(ch - b'a') as usize] + MOD) % MOD;
        }
        ((total - 1 + MOD) % MOD) as i32
    }
}
