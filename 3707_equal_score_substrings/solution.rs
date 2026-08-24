// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

impl Solution {
    pub fn score_balance(s: String) -> bool {
        let bytes = s.as_bytes();
        let mut l = 0;
        let mut r: i32 = bytes.iter().map(|&c| (c - b'a') as i32 + 1).sum();
        for i in 0..bytes.len().saturating_sub(1) {
            let x = (bytes[i] - b'a') as i32 + 1;
            l += x;
            r -= x;
            if l == r {
                return true;
            }
        }
        false
    }
}
