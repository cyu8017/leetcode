// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

impl Solution {
    pub fn print_vertically(s: String) -> Vec<String> {
        let words: Vec<&str> = s.split_whitespace().collect();
        let max_len = words.iter().map(|w| w.len()).max().unwrap_or(0);
        (0..max_len)
            .map(|i| {
                words
                    .iter()
                    .map(|w| w.chars().nth(i).unwrap_or(' '))
                    .collect::<String>()
                    .trim_end()
                    .to_string()
            })
            .collect()
    }
}
