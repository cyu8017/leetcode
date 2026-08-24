// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

use std::collections::HashSet;

impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        const CODES: [&str; 26] = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
            ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
            ".--", "-..-", "-.--", "--..",
        ];
        let mut seen = HashSet::new();
        for word in &words {
            let mut code = String::new();
            for ch in word.bytes() {
                code.push_str(CODES[(ch - b'a') as usize]);
            }
            seen.insert(code);
        }
        seen.len() as i32
    }
}
