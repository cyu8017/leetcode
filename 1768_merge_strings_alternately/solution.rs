// LeetCode 1768 - Merge Strings Alternately
// https://leetcode.com/problems/merge-strings-alternately/

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let a: Vec<char> = word1.chars().collect();
        let b: Vec<char> = word2.chars().collect();
        let mut out = String::with_capacity(a.len() + b.len());
        let mut i = 0;
        let mut j = 0;
        while i < a.len() || j < b.len() {
            if i < a.len() {
                out.push(a[i]);
                i += 1;
            }
            if j < b.len() {
                out.push(b[j]);
                j += 1;
            }
        }
        out
    }
}
