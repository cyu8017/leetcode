// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

use std::collections::HashMap;

impl Solution {
    pub fn original_digits(s: String) -> String {
        let mut counts: HashMap<char, i32> = HashMap::new();
        for ch in s.chars() {
            *counts.entry(ch).or_insert(0) += 1;
        }

        let mut digit_counts = [0_i32; 10];
        digit_counts[0] = *counts.get(&'z').unwrap_or(&0);
        digit_counts[2] = *counts.get(&'w').unwrap_or(&0);
        digit_counts[4] = *counts.get(&'u').unwrap_or(&0);
        digit_counts[6] = *counts.get(&'x').unwrap_or(&0);
        digit_counts[8] = *counts.get(&'g').unwrap_or(&0);
        digit_counts[1] =
            counts.get(&'o').unwrap_or(&0) - digit_counts[0] - digit_counts[2] - digit_counts[4];
        digit_counts[3] = counts.get(&'h').unwrap_or(&0) - digit_counts[8];
        digit_counts[5] = counts.get(&'f').unwrap_or(&0) - digit_counts[4];
        digit_counts[7] = counts.get(&'s').unwrap_or(&0) - digit_counts[6];
        digit_counts[9] = counts.get(&'i').unwrap_or(&0)
            - digit_counts[5]
            - digit_counts[6]
            - digit_counts[8];

        let mut result = String::new();
        for digit in 0..10 {
            for _ in 0..digit_counts[digit] {
                result.push((b'0' + digit as u8) as char);
            }
        }
        result
    }
}
