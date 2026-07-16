// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

use std::collections::HashMap;

impl Solution {
    pub fn word_squares(words: Vec<String>) -> Vec<Vec<String>> {
        let mut words = words;
        words.sort();
        let length = words[0].len();
        let mut prefix_map: HashMap<String, Vec<String>> = HashMap::new();
        prefix_map.insert(String::new(), words.clone());

        for word in &words {
            for index in 0..word.len() {
                let prefix = word[..=index].to_string();
                prefix_map
                    .entry(prefix)
                    .or_default()
                    .push(word.clone());
            }
        }

        let mut squares: Vec<Vec<String>> = Vec::new();
        let mut current: Vec<String> = Vec::new();

        fn dfs(
            row: usize,
            length: usize,
            prefix_map: &HashMap<String, Vec<String>>,
            current: &mut Vec<String>,
            squares: &mut Vec<Vec<String>>,
        ) {
            if row == length {
                squares.push(current.clone());
                return;
            }

            let prefix: String = current.iter().map(|word| word.as_bytes()[row] as char).collect();
            if let Some(candidates) = prefix_map.get(&prefix) {
                for candidate in candidates {
                    current.push(candidate.clone());
                    dfs(row + 1, length, prefix_map, current, squares);
                    current.pop();
                }
            }
        }

        dfs(0, length, &prefix_map, &mut current, &mut squares);
        squares
    }
}
