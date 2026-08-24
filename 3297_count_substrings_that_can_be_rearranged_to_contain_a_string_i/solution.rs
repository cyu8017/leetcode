// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

impl Solution {
    pub fn valid_substring_count(word1: String, word2: String) -> i64 {
        let mut need = [0i32; 26];
        let mut required = 0;
        for c in word2.bytes() {
            let i = (c - b'a') as usize;
            if need[i] == 0 {
                required += 1;
            }
            need[i] += 1;
        }
        let mut have = [0i32; 26];
        let mut formed = 0;
        let mut ans = 0i64;
        let mut l = 0usize;
        let w = word1.as_bytes();
        for r in 0..w.len() {
            let c = (w[r] - b'a') as usize;
            have[c] += 1;
            if have[c] == need[c] && need[c] > 0 {
                formed += 1;
            }
            while formed == required && l <= r {
                ans += (w.len() - r) as i64;
                let c2 = (w[l] - b'a') as usize;
                if have[c2] == need[c2] && need[c2] > 0 {
                    formed -= 1;
                }
                have[c2] -= 1;
                l += 1;
            }
        }
        ans
    }
}
