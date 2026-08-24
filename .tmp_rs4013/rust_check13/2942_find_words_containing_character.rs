#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let mut ans = Vec::new();
        for (i, w) in words.iter().enumerate() {
            if w.contains(x) {
                ans.push(i as i32);
            }
        }
        ans
    }
}
