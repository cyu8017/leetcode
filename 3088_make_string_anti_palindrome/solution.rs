// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

impl Solution {
    pub fn make_anti_palindrome(s: String) -> String {
        let mut s: Vec<u8> = s.into_bytes();
        s.sort_unstable();
        let n = s.len();
        let m = n / 2;
        if s[m] == s[m - 1] {
            let mut i = m;
            while i < n && s[i] == s[i - 1] {
                i += 1;
            }
            let mut j = m;
            while j < n && s[j] == s[n - j - 1] {
                if i >= n {
                    return "-1".to_string();
                }
                s.swap(i, j);
                i += 1;
                j += 1;
            }
        }
        String::from_utf8(s).unwrap()
    }
}
