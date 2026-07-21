// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

use std::collections::HashMap;

impl Solution {
    pub fn evaluate(s: String, knowledge: Vec<Vec<String>>) -> String {
        let lookup: HashMap<&str, &str> = knowledge
            .iter()
            .map(|pair| (pair[0].as_str(), pair[1].as_str()))
            .collect();
        let mut result = String::new();
        let chars: Vec<char> = s.chars().collect();
        let mut i = 0;
        while i < chars.len() {
            if chars[i] == '(' {
                let mut j = i + 1;
                while j < chars.len() && chars[j] != ')' {
                    j += 1;
                }
                let key: String = chars[i + 1..j].iter().collect();
                result.push_str(lookup.get(key.as_str()).copied().unwrap_or("?"));
                i = j + 1;
            } else {
                result.push(chars[i]);
                i += 1;
            }
        }
        result
    }
}
