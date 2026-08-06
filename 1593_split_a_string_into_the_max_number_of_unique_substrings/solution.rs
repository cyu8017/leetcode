// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

use std::collections::HashSet;

impl Solution {
    pub fn max_unique_split(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut used = HashSet::new();
        let mut answer = 0;
        fn dfs(i: usize, bytes: &[u8], used: &mut HashSet<String>, answer: &mut i32) {
            if used.len() + bytes.len() - i <= *answer as usize {
                return;
            }
            if i == bytes.len() {
                *answer = (*answer).max(used.len() as i32);
                return;
            }
            for j in i + 1..=bytes.len() {
                let part = String::from_utf8(bytes[i..j].to_vec()).unwrap();
                if used.insert(part.clone()) {
                    dfs(j, bytes, used, answer);
                    used.remove(&part);
                }
            }
        }
        dfs(0, bytes, &mut used, &mut answer);
        answer
    }
}
