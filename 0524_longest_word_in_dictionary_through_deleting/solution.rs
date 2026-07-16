// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

impl Solution {
    pub fn find_longest_word(s: String, dictionary: Vec<String>) -> String {
        fn is_subsequence(word: &str, source: &str) -> bool {
            let mut index = 0;
            for ch in source.chars() {
                if index < word.len() && word.as_bytes()[index] == ch as u8 {
                    index += 1;
                }
            }
            index == word.len()
        }

        let mut best = String::new();
        for word in dictionary {
            if !is_subsequence(&word, &s) {
                continue;
            }
            if word.len() > best.len() || (word.len() == best.len() && word < best) {
                best = word;
            }
        }
        best
    }
}
