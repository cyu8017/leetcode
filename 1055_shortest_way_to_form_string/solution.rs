// LeetCode 1055 - Shortest Way to Form String
// https://leetcode.com/problems/shortest-way-to-form-string/

use std::collections::HashSet;

impl Solution {
    pub fn shortest_way(source: String, target: String) -> i32 {
        let source_set: HashSet<u8> = source.bytes().collect();
        let target_bytes = target.as_bytes();
        if target_bytes.iter().any(|ch| !source_set.contains(ch)) {
            return -1;
        }
        let mut ans = 0;
        let mut i = 0;
        let n = target_bytes.len();
        while i < n {
            ans += 1;
            for ch in source.bytes() {
                if i < n && target_bytes[i] == ch {
                    i += 1;
                }
            }
        }
        ans
    }
}
