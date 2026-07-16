// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut stack: Vec<String> = Vec::new();

        for part in path.split('/') {
            if part.is_empty() || part == "." {
                continue;
            }
            if part == ".." {
                stack.pop();
            } else {
                stack.push(part.to_string());
            }
        }

        format!("/{}", stack.join("/"))
    }
}
