// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

impl Solution {
    pub fn is_valid(code: String) -> bool {
        let chars: Vec<char> = code.chars().collect();
        let n = chars.len();
        let mut stack = Vec::new();
        let mut i = 0;
        while i < n {
            let rest: String = chars[i..].iter().collect();
            if rest.starts_with("<![CDATA[") {
                if stack.is_empty() {
                    return false;
                }
                if let Some(j) = rest.find("]]>") {
                    i += j + 3;
                } else {
                    return false;
                }
            } else if rest.starts_with("</") {
                if let Some(j) = rest[2..].find('>') {
                    let tag: String = rest[2..2 + j].to_string();
                    if stack.last() != Some(&tag) {
                        return false;
                    }
                    stack.pop();
                    i += 2 + j + 1;
                    if stack.is_empty() && i < n {
                        return false;
                    }
                } else {
                    return false;
                }
            } else if chars[i] == '<' {
                if let Some(j) = rest[1..].find('>') {
                    let tag: String = rest[1..1 + j].to_string();
                    if tag.is_empty() || tag.len() > 9 {
                        return false;
                    }
                    if !tag.chars().all(|ch| ch.is_ascii_uppercase()) {
                        return false;
                    }
                    stack.push(tag);
                    i += 1 + j + 1;
                } else {
                    return false;
                }
            } else {
                if stack.is_empty() {
                    return false;
                }
                i += 1;
            }
        }
        stack.is_empty()
    }
}
