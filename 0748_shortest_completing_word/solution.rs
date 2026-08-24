// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

impl Solution {
    pub fn shortest_completing_word(license_plate: String, words: Vec<String>) -> String {
        let mut need = [0i32; 26];
        for ch in license_plate.bytes() {
            if ch.is_ascii_alphabetic() {
                need[(ch.to_ascii_lowercase() - b'a') as usize] += 1;
            }
        }
        let mut best = String::new();
        for word in words {
            let mut counts = [0i32; 26];
            for ch in word.bytes() {
                counts[(ch - b'a') as usize] += 1;
            }
            if (0..26).all(|i| counts[i] >= need[i]) && (best.is_empty() || word.len() < best.len())
            {
                best = word;
            }
        }
        best
    }
}
