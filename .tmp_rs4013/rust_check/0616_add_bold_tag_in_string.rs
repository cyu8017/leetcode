struct Solution;
// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

impl Solution {
    pub fn add_bold_tag(s: String, words: Vec<String>) -> String {
        let n = s.len();
        let mut bold = vec![false; n];
        for word in &words {
            let mut start = 0;
            while let Some(pos) = s[start..].find(word) {
                let abs = start + pos;
                for i in abs..abs + word.len() {
                    bold[i] = true;
                }
                start = abs + 1;
            }
        }
        let bytes = s.as_bytes();
        let mut parts = String::new();
        let mut i = 0;
        while i < n {
            if bold[i] {
                parts.push_str("<b>");
                while i < n && bold[i] {
                    parts.push(bytes[i] as char);
                    i += 1;
                }
                parts.push_str("</b>");
            } else {
                parts.push(bytes[i] as char);
                i += 1;
            }
        }
        parts
    }
}

fn main() {}
