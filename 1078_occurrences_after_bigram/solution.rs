// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

impl Solution {
    pub fn find_ocurrences(text: String, first: String, second: String) -> Vec<String> {
        let words: Vec<&str> = text.split_whitespace().collect();
        let mut ans = Vec::new();
        for i in 0..words.len().saturating_sub(2) {
            if words[i] == first && words[i + 1] == second {
                ans.push(words[i + 2].to_string());
            }
        }
        ans
    }
}
