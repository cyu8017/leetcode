// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

use std::collections::HashSet;

impl Solution {
    pub fn before_and_after_puzzles(phrases: Vec<String>) -> Vec<String> {
        let split: Vec<Vec<&str>> = phrases.iter().map(|p| p.split_whitespace().collect()).collect();
        let mut result = HashSet::new();
        for i in 0..split.len() {
            for j in 0..split.len() {
                if i == j {
                    continue;
                }
                if split[i].last() == split[j].first() {
                    let mut merged = split[i].clone();
                    merged.extend_from_slice(&split[j][1..]);
                    result.insert(merged.join(" "));
                }
            }
        }
        let mut ans: Vec<String> = result.into_iter().collect();
        ans.sort();
        ans
    }
}
