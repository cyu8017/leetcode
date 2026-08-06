// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

impl Solution {
    pub fn reorder_spaces(text: String) -> String {
        let words: Vec<&str> = text.split_whitespace().collect();
        let spaces = text.bytes().filter(|&c| c == b' ').count();
        if words.len() == 1 {
            return format!("{}{}", words[0], " ".repeat(spaces));
        }
        let between = spaces / (words.len() - 1);
        let trailing = spaces % (words.len() - 1);
        format!("{}{}", words.join(&" ".repeat(between)), " ".repeat(trailing))
    }
}
