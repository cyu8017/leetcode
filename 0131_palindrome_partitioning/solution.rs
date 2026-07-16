// LeetCode 0131 - Palindrome Partitioning
impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        fn dfs(bytes: &[u8], start: usize, path: &mut Vec<String>, result: &mut Vec<Vec<String>>) {
            if start == bytes.len() { result.push(path.clone()); return; }
            for end in start..bytes.len() {
                if bytes[start..=end].iter().eq(bytes[start..=end].iter().rev()) {
                    path.push(String::from_utf8(bytes[start..=end].to_vec()).unwrap());
                    dfs(bytes, end + 1, path, result);
                    path.pop();
                }
            }
        }
        let mut result = Vec::new();
        dfs(s.as_bytes(), 0, &mut Vec::new(), &mut result);
        result
    }
}