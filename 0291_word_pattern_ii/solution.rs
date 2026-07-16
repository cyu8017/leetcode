// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

use std::collections::HashMap;

impl Solution {
    pub fn word_pattern_match(pattern: String, s: String) -> bool {
        let pattern = pattern.as_bytes();
        let s = s.as_bytes();
        let mut char_to_word: HashMap<u8, &str> = HashMap::new();
        let mut word_to_char: HashMap<&str, u8> = HashMap::new();

        fn backtrack(
            pattern: &[u8],
            s: &[u8],
            pattern_index: usize,
            string_index: usize,
            char_to_word: &mut HashMap<u8, &str>,
            word_to_char: &mut HashMap<&str, u8>,
        ) -> bool {
            if pattern_index == pattern.len() {
                return string_index == s.len();
            }

            let ch = pattern[pattern_index];
            if let Some(word) = char_to_word.get(&ch) {
                let word_bytes = word.as_bytes();
                if string_index + word_bytes.len() > s.len()
                    || &s[string_index..string_index + word_bytes.len()] != word_bytes
                {
                    return false;
                }
                return backtrack(
                    pattern,
                    s,
                    pattern_index + 1,
                    string_index + word_bytes.len(),
                    char_to_word,
                    word_to_char,
                );
            }

            for end in (string_index + 1)..=s.len() {
                let word = std::str::from_utf8(&s[string_index..end]).unwrap();
                if word_to_char.contains_key(word) {
                    continue;
                }
                char_to_word.insert(ch, word);
                word_to_char.insert(word, ch);
                if backtrack(
                    pattern,
                    s,
                    pattern_index + 1,
                    end,
                    char_to_word,
                    word_to_char,
                ) {
                    return true;
                }
                char_to_word.remove(&ch);
                word_to_char.remove(word);
            }
            false
        }

        backtrack(pattern, s, 0, 0, &mut char_to_word, &mut word_to_char)
    }
}
