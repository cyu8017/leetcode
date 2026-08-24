struct Solution;
fn main() {}

// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

impl Solution {
    pub fn smallest_string(s: String) -> String {
        let mut b = s.into_bytes();
        let n = b.len();
        let mut i = 0;
        while i < n && b[i] == b'a' {
            i += 1;
        }
        if i == n {
            b[n - 1] = b'z';
            return String::from_utf8(b).unwrap();
        }
        while i < n && b[i] != b'a' {
            b[i] -= 1;
            i += 1;
        }
        String::from_utf8(b).unwrap()
    }
}
