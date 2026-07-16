// LeetCode 0408 - Valid Word Abbreviation
// https://leetcode.com/problems/valid-word-abbreviation/

impl Solution {
    pub fn valid_word_abbreviation(word: String, abbr: String) -> bool {
        let word_bytes = word.as_bytes();
        let abbr_bytes = abbr.as_bytes();
        let mut word_index = 0;
        let mut abbr_index = 0;

        while word_index < word_bytes.len() && abbr_index < abbr_bytes.len() {
            if abbr_bytes[abbr_index].is_ascii_digit() {
                if abbr_bytes[abbr_index] == b'0' {
                    return false;
                }

                let mut number = 0;
                while abbr_index < abbr_bytes.len() && abbr_bytes[abbr_index].is_ascii_digit() {
                    number = number * 10 + (abbr_bytes[abbr_index] - b'0') as i32;
                    abbr_index += 1;
                }
                word_index += number as usize;
            } else {
                if word_bytes[word_index] != abbr_bytes[abbr_index] {
                    return false;
                }
                word_index += 1;
                abbr_index += 1;
            }
        }

        word_index == word_bytes.len() && abbr_index == abbr_bytes.len()
    }
}
