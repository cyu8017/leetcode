// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

impl Solution {
    pub fn sort_sentence(s: String) -> String {
        let tokens: Vec<&str> = s.split_whitespace().collect();
        let mut ordered = vec![String::new(); tokens.len()];
        for token in tokens {
            let position = token.as_bytes()[token.len() - 1] as usize - b'1' as usize;
            ordered[position] = token[..token.len() - 1].to_string();
        }
        ordered.join(" ")
    }
}
