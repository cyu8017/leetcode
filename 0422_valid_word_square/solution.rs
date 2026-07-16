// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

impl Solution {
    pub fn valid_word_square(words: Vec<String>) -> bool {
        for (row, word) in words.iter().enumerate() {
            for (col, ch) in word.chars().enumerate() {
                if col >= words.len()
                    || row >= words[col].len()
                    || words[col].as_bytes()[row] != ch as u8
                {
                    return false;
                }
            }
        }
        true
    }
}
