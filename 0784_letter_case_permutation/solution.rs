// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

impl Solution {
    pub fn letter_case_permutation(s: String) -> Vec<String> {
        let mut result = vec![String::new()];
        for ch in s.chars() {
            let mut next = Vec::new();
            if ch.is_ascii_alphabetic() {
                let lower = ch.to_ascii_lowercase();
                let upper = ch.to_ascii_uppercase();
                for prefix in result {
                    next.push(format!("{prefix}{lower}"));
                    next.push(format!("{prefix}{upper}"));
                }
            } else {
                for prefix in result {
                    next.push(format!("{prefix}{ch}"));
                }
            }
            result = next;
        }
        result
    }
}
