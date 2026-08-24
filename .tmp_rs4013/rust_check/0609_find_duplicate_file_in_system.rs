struct Solution;
// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

use std::collections::HashMap;

impl Solution {
    pub fn find_duplicate(paths: Vec<String>) -> Vec<Vec<String>> {
        let mut content_to_paths: HashMap<String, Vec<String>> = HashMap::new();
        for entry in paths {
            let mut parts = entry.split_whitespace();
            let directory = parts.next().unwrap();
            for file_info in parts {
                let open = file_info.find('(').unwrap();
                let name = &file_info[..open];
                let content = &file_info[open + 1..file_info.len() - 1];
                content_to_paths
                    .entry(content.to_string())
                    .or_default()
                    .push(format!("{}/{}", directory, name));
            }
        }
        content_to_paths
            .into_values()
            .filter(|group| group.len() > 1)
            .collect()
    }
}

fn main() {}
