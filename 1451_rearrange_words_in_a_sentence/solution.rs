// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

impl Solution {
    pub fn arrange_words(text: String) -> String {
        let mut words: Vec<String> = text.to_lowercase().split_whitespace().map(|s| s.to_string()).collect();
        words.sort_by_key(|w| w.len());
        let mut s = words.join(" ");
        if let Some(first) = s.get_mut(0..1) {
            first.make_ascii_uppercase();
        }
        s
    }
}
