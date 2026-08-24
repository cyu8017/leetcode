// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

impl Solution {
    pub fn is_substring_present(s: String) -> bool {
        let b = s.as_bytes();
        let mut st = [[false; 26]; 26];
        for i in 0..b.len().saturating_sub(1) {
            st[(b[i + 1] - b'a') as usize][(b[i] - b'a') as usize] = true;
        }
        for i in 0..b.len().saturating_sub(1) {
            if st[(b[i] - b'a') as usize][(b[i + 1] - b'a') as usize] {
                return true;
            }
        }
        false
    }
}
