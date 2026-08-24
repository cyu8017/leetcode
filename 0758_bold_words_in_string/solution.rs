// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

impl Solution {
    pub fn bold_words(words: Vec<String>, s: String) -> String {
        let n = s.len();
        let mut bold = vec![false; n];
        for word in &words {
            let mut start = s.find(word.as_str());
            while let Some(idx) = start {
                for i in idx..idx + word.len() {
                    bold[i] = true;
                }
                start = s[idx + 1..].find(word.as_str()).map(|p| p + idx + 1);
            }
        }
        let bytes = s.as_bytes();
        let mut parts = String::new();
        let mut i = 0;
        while i < n {
            if bold[i] {
                parts.push_str("**");
                while i < n && bold[i] {
                    parts.push(bytes[i] as char);
                    i += 1;
                }
                parts.push_str("**");
            } else {
                parts.push(bytes[i] as char);
                i += 1;
            }
        }
        parts
    }
}
