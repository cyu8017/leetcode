// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let n = n as usize;
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn backtrack(
            path: &mut Vec<u8>,
            result: &mut Vec<String>,
            open: usize,
            close: usize,
            n: usize,
        ) {
            if path.len() == 2 * n {
                result.push(String::from_utf8(path.clone()).unwrap());
                return;
            }
            if open < n {
                path.push(b'(');
                backtrack(path, result, open + 1, close, n);
                path.pop();
            }
            if close < open {
                path.push(b')');
                backtrack(path, result, open, close + 1, n);
                path.pop();
            }
        }

        backtrack(&mut path, &mut result, 0, 0, n);
        result
    }
}
