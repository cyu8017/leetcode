// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

use std::collections::VecDeque;

impl Solution {
    pub fn is_transformable(s: String, t: String) -> bool {
        let mut positions: Vec<VecDeque<usize>> = vec![VecDeque::new(); 10];
        for (i, ch) in s.bytes().enumerate() {
            positions[(ch - b'0') as usize].push_back(i);
        }
        for ch in t.bytes() {
            let d = (ch - b'0') as usize;
            if positions[d].is_empty() {
                return false;
            }
            let index = positions[d][0];
            for smaller in 0..d {
                if positions[smaller]
                    .front()
                    .map_or(false, |&pos| pos < index)
                {
                    return false;
                }
            }
            positions[d].pop_front();
        }
        true
    }
}
