// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let chars: Vec<char> = word.chars().collect();
        let all_upper = chars.iter().all(|ch| ch.is_uppercase());
        let all_lower = chars.iter().all(|ch| ch.is_lowercase());
        if all_upper || all_lower {
            return true;
        }
        chars[1..].iter().all(|ch| ch.is_lowercase()) && chars[0].is_uppercase()
    }
}
