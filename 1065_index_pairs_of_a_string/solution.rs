// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

use std::collections::HashSet;

impl Solution {
    pub fn index_pairs(text: String, words: Vec<String>) -> Vec<Vec<i32>> {
        let word_set: HashSet<&str> = words.iter().map(|s| s.as_str()).collect();
        let mut ans = Vec::new();
        let n = text.len();
        for i in 0..n {
            for j in i..n {
                if word_set.contains(&text[i..=j]) {
                    ans.push(vec![i as i32, j as i32]);
                }
            }
        }
        ans
    }
}
