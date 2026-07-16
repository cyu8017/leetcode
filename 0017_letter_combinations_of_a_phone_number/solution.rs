// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

const MAPPING: [&str; 10] = [
    "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz",
];

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return Vec::new();
        }

        let digits: Vec<u8> = digits.bytes().collect();
        let mut result = Vec::new();
        let mut path = Vec::new();

        fn backtrack(
            digits: &[u8],
            index: usize,
            path: &mut Vec<u8>,
            result: &mut Vec<String>,
        ) {
            if index == digits.len() {
                result.push(String::from_utf8(path.clone()).unwrap());
                return;
            }
            for ch in MAPPING[(digits[index] - b'0') as usize].bytes() {
                path.push(ch);
                backtrack(digits, index + 1, path, result);
                path.pop();
            }
        }

        backtrack(&digits, 0, &mut path, &mut result);
        result
    }
}
