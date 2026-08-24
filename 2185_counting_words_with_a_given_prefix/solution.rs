// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

impl Solution {
    pub fn prefix_count(words: Vec<String>, pref: String) -> i32 {
        words.iter().filter(|w| w.starts_with(&pref)).count() as i32
    }
}
