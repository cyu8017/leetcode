// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

impl Solution {
    pub fn largest_even(s: String) -> String {
        let mut bytes = s.into_bytes();
        while bytes.last() == Some(&b'1') {
            bytes.pop();
        }
        String::from_utf8(bytes).unwrap()
    }
}
