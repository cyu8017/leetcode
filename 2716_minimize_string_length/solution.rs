// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

use std::collections::HashSet;

impl Solution {
    pub fn minimized_string_length(s: String) -> i32 {
        s.chars().collect::<HashSet<_>>().len() as i32
    }
}
