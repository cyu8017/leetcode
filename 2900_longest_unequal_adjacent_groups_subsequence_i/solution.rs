// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let mut ans = vec![words[0].clone()];
        let mut last = groups[0];
        for i in 1..words.len() {
            if groups[i] != last {
                ans.push(words[i].clone());
                last = groups[i];
            }
        }
        ans
    }
}
