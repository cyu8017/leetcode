// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

use std::collections::HashMap;

impl Solution {
    pub fn longest_awesome(s: String) -> i32 {
        let mut first = HashMap::new();
        first.insert(0, -1);
        let mut mask = 0;
        let mut answer = 0;
        for (i, ch) in s.bytes().enumerate() {
            mask ^= 1 << (ch - b'0');
            if let Some(&idx) = first.get(&mask) {
                answer = answer.max(i as i32 - idx);
            } else {
                first.insert(mask, i as i32);
            }
            for bit in 0..10 {
                let candidate = mask ^ (1 << bit);
                if let Some(&idx) = first.get(&candidate) {
                    answer = answer.max(i as i32 - idx);
                }
            }
        }
        answer
    }
}
