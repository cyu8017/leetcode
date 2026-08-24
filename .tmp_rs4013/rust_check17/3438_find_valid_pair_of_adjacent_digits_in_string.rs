struct Solution;
// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

impl Solution {
    pub fn find_valid_pair(s: String) -> String {
        let bytes = s.as_bytes();
        let mut freq = [0i32; 10];
        for &c in bytes {
            freq[(c - b'0') as usize] += 1;
        }
        for i in 0..bytes.len().saturating_sub(1) {
            let a = (bytes[i] - b'0') as i32;
            let b = (bytes[i + 1] - b'0') as i32;
            if a != b && freq[a as usize] == a && freq[b as usize] == b {
                return s[i..i + 2].to_string();
            }
        }
        String::new()
    }
}

fn main() {}
