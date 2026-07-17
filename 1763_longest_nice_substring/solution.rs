// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

impl Solution {
    pub fn longest_nice_substring(s: String) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut best_start = 0;
        let mut best_len = 0;
        for i in 0..n {
            let mut lower: u32 = 0;
            let mut upper: u32 = 0;
            for j in i..n {
                let c = bytes[j];
                if c.is_ascii_lowercase() {
                    lower |= 1 << (c - b'a');
                } else {
                    upper |= 1 << (c - b'A');
                }
                if lower == upper && j - i + 1 > best_len {
                    best_start = i;
                    best_len = j - i + 1;
                }
            }
        }
        s[best_start..best_start + best_len].to_string()
    }
}
