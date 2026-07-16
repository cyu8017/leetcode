// LeetCode 0186 - Reverse Words in a String II
// https://leetcode.com/problems/reverse-words-in-a-string-ii/

impl Solution {
    pub fn reverse_words(s: &mut Vec<char>) {
        s.reverse();
        let mut start = 0;
        for end in 0..=s.len() {
            if end == s.len() || s[end] == ' ' {
                s[start..end].reverse();
                start = end + 1;
            }
        }
    }
}