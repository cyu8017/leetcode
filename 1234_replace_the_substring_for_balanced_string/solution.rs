// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

use std::collections::HashMap;

impl Solution {
    pub fn balanced_string(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut count = HashMap::new();
        for &ch in bytes {
            *count.entry(ch).or_insert(0) += 1;
        }
        let limit = bytes.len() / 4;
        let n = bytes.len();
        let mut left = 0usize;
        let mut answer = n;
        let ok = |count: &HashMap<u8, i32>| {
            for c in [b'Q', b'W', b'E', b'R'] {
                if *count.get(&c).unwrap_or(&0) > limit as i32 {
                    return false;
                }
            }
            true
        };
        for right in 0..n {
            *count.entry(bytes[right]).or_insert(0) -= 1;
            while left <= right && ok(&count) {
                answer = answer.min(right - left + 1);
                *count.entry(bytes[left]).or_insert(0) += 1;
                left += 1;
            }
        }
        answer as i32
    }
}
