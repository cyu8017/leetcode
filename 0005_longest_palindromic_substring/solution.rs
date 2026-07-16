// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let bytes = s.as_bytes();
        let mut best_start = 0usize;
        let mut best_len = 0usize;

        let mut expand = |left: isize, right: isize| {
            let mut l = left;
            let mut r = right;
            while l >= 0
                && (r as usize) < bytes.len()
                && bytes[l as usize] == bytes[r as usize]
            {
                l -= 1;
                r += 1;
            }
            let len = (r - l - 1) as usize;
            if len > best_len {
                best_len = len;
                best_start = (l + 1) as usize;
            }
        };

        for i in 0..bytes.len() {
            expand(i as isize, i as isize);
            expand(i as isize, i as isize + 1);
        }

        String::from_utf8(bytes[best_start..best_start + best_len].to_vec()).unwrap()
    }
}
