// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

impl Solution {
    pub fn capitalize_title(title: String) -> String {
        title
            .split_whitespace()
            .map(|w| {
                let mut w = w.to_lowercase();
                if w.len() > 2 {
                    let mut chars: Vec<char> = w.chars().collect();
                    chars[0] = chars[0].to_ascii_uppercase();
                    w = chars.into_iter().collect();
                }
                w
            })
            .collect::<Vec<_>>()
            .join(" ")
    }
}
