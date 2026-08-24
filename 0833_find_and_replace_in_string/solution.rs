// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

use std::collections::HashMap;

impl Solution {
    pub fn find_replace_string(
        s: String,
        indices: Vec<i32>,
        sources: Vec<String>,
        targets: Vec<String>,
    ) -> String {
        let mut replace = HashMap::new();
        for k in 0..indices.len() {
            let i = indices[k] as usize;
            if s.get(i..i + sources[k].len()) == Some(sources[k].as_str()) {
                replace.insert(i, (sources[k].len(), targets[k].clone()));
            }
        }
        let mut out = String::new();
        let mut i = 0;
        let n = s.len();
        while i < n {
            if let Some(&(len, ref target)) = replace.get(&i) {
                out.push_str(target);
                i += len;
            } else {
                out.push(s.as_bytes()[i] as char);
                i += 1;
            }
        }
        out
    }
}
