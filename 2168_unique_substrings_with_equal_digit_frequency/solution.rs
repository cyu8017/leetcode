// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

use std::collections::HashSet;

impl Solution {
    pub fn equal_digit_frequency(s: String) -> i32 {
        let n = s.len();
        let b = s.as_bytes();
        let mut seen = HashSet::new();
        for i in 0..n {
            let mut freq = [0i32; 10];
            let mut maxf = 0;
            let mut kinds = 0;
            for j in i..n {
                let d = (b[j] - b'0') as usize;
                if freq[d] == 0 {
                    kinds += 1;
                }
                freq[d] += 1;
                maxf = maxf.max(freq[d]);
                if maxf * kinds == (j - i + 1) as i32 {
                    seen.insert(&s[i..=j]);
                }
            }
        }
        seen.len() as i32
    }
}
