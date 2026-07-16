// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

impl Solution {
    pub fn license_key_formatting(s: String, k: i32) -> String {
        let k = k as usize;
        let chars: Vec<char> = s
            .chars()
            .filter(|ch| *ch != '-')
            .map(|ch| ch.to_ascii_uppercase())
            .collect();
        if chars.is_empty() {
            return String::new();
        }
        let first_len = if chars.len() % k == 0 {
            k
        } else {
            chars.len() % k
        };
        let mut parts = vec![chars[..first_len].iter().collect::<String>()];
        let mut index = first_len;
        while index < chars.len() {
            parts.push(chars[index..index + k].iter().collect());
            index += k;
        }
        parts.join("-")
    }
}
