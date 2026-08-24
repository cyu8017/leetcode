struct Solution;
// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

use std::collections::HashMap;

impl Solution {
    pub fn count_word_occurrences(chunks: Vec<String>, queries: Vec<String>) -> Vec<i32> {
        let s = chunks.concat();
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut cnt: HashMap<String, i32> = HashMap::new();
        let mut i = 0;
        while i < n {
            if bytes[i] == b' ' || bytes[i] == b'-' {
                i += 1;
                continue;
            }
            let mut j = i;
            while j < n
                && bytes[j] != b' '
                && !(bytes[j] == b'-'
                    && (j + 1 >= n || bytes[j + 1] == b' ' || bytes[j + 1] == b'-'))
            {
                j += 1;
            }
            *cnt.entry(s[i..j].to_string()).or_insert(0) += 1;
            i = j;
        }
        queries
            .into_iter()
            .map(|q| *cnt.get(&q).unwrap_or(&0))
            .collect()
    }
}

fn main() {}
