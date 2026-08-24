// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        let n = word.len();
        let bytes = word.as_bytes();
        let mut p = vec![0i64; n + 1];
        let mut h = vec![0i64; n + 1];
        let base = 13331i64;
        let modulus = 998244353i64;
        p[0] = 1;
        for i in 1..=n {
            p[i] = p[i - 1] * base % modulus;
            h[i] = (h[i - 1] * base + (bytes[i - 1] - b'a') as i64) % modulus;
        }
        let query = |l: usize, r: usize| -> i64 {
            (h[r] - h[l - 1] * p[r - l + 1] % modulus + modulus) % modulus
        };
        let k = k as usize;
        let mut i = k;
        while i < n {
            if query(1, n - i) == query(i + 1, n) {
                return (i / k) as i32;
            }
            i += k;
        }
        ((n + k - 1) / k) as i32
    }
}
