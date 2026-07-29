// LeetCode 1016 - Binary String With Substrings Representing 1 To N
// https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

impl Solution {
    pub fn query_string(s: String, n: i32) -> bool {
        for i in (n / 2 + 1)..=n {
            let bin = format!("{:b}", i);
            if !s.contains(&bin) {
                return false;
            }
        }
        true
    }
}
