struct Solution;
fn main() {}

// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

impl Solution {
    pub fn replicate(s: String, times: i32) -> String {
        if times <= 0 {
            return String::new();
        }
        s.repeat(times as usize)
    }
}
