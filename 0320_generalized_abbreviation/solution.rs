// LeetCode 0320 - Generalized Abbreviation
// https://leetcode.com/problems/generalized-abbreviation/

impl Solution {
    pub fn generate_abbreviations(word: String) -> Vec<String> {
        let bytes = word.as_bytes();
        let mut result = Vec::new();

        fn backtrack(
            word: &[u8],
            index: usize,
            path: String,
            count: i32,
            result: &mut Vec<String>,
        ) {
            if index == word.len() {
                if count > 0 {
                    result.push(format!("{path}{count}"));
                } else {
                    result.push(path);
                }
                return;
            }
            backtrack(word, index + 1, path, count + 1, result);
            let mut next_path = path;
            if count > 0 {
                next_path.push_str(&count.to_string());
            }
            next_path.push(word[index] as char);
            backtrack(word, index + 1, next_path, 0, result);
        }

        backtrack(bytes, 0, String::new(), 0, &mut result);
        result
    }
}
