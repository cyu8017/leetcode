// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

use std::collections::HashMap;

impl Solution {
    pub fn group_strings(strings: Vec<String>) -> Vec<Vec<String>> {
        let mut groups: HashMap<String, Vec<String>> = HashMap::new();
        let mut order: Vec<String> = Vec::new();

        for text in strings {
            let key = if text.is_empty() {
                String::new()
            } else {
                let base = text.as_bytes()[0] as i32;
                text.bytes()
                    .map(|byte| ((byte as i32 - base + 26) % 26).to_string())
                    .collect::<Vec<_>>()
                    .join(",")
            };
            if !groups.contains_key(&key) {
                order.push(key.clone());
                groups.insert(key.clone(), Vec::new());
            }
            groups.get_mut(&key).unwrap().push(text);
        }

        order
            .into_iter()
            .map(|key| groups.remove(&key).unwrap())
            .collect()
    }
}
