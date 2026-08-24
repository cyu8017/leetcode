// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

impl Solution {
    pub fn remove_comments(source: Vec<String>) -> Vec<String> {
        let mut result = Vec::new();
        let mut buffer = String::new();
        let mut in_block = false;
        for line in source {
            let chars: Vec<char> = line.chars().collect();
            let mut i = 0;
            while i < chars.len() {
                if in_block {
                    if i + 1 < chars.len() && chars[i] == '*' && chars[i + 1] == '/' {
                        in_block = false;
                        i += 2;
                    } else {
                        i += 1;
                    }
                } else if i + 1 < chars.len() && chars[i] == '/' && chars[i + 1] == '*' {
                    in_block = true;
                    i += 2;
                } else if i + 1 < chars.len() && chars[i] == '/' && chars[i + 1] == '/' {
                    break;
                } else {
                    buffer.push(chars[i]);
                    i += 1;
                }
            }
            if !in_block && !buffer.is_empty() {
                result.push(std::mem::take(&mut buffer));
            }
        }
        result
    }
}
