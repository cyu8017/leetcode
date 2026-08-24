struct Solution;
fn main() {}

// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

impl Solution {
    pub fn can_make_subsequence(str1: String, str2: String) -> bool {
        let a = str1.as_bytes();
        let b = str2.as_bytes();
        let mut j = 0;
        for &c in a {
            if j == b.len() {
                break;
            }
            if c == b[j] || (c - b'a' + 1) % 26 == b[j] - b'a' {
                j += 1;
            }
        }
        j == b.len()
    }
}
