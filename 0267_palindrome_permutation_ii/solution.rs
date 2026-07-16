// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

use std::collections::HashMap;

impl Solution {
    pub fn generate_palindromes(s: String) -> Vec<String> {
        let mut counts = HashMap::new();
        for byte in s.bytes() {
            *counts.entry(byte).or_insert(0usize) += 1;
        }

        let odd_chars: Vec<u8> = counts
            .iter()
            .filter(|(_, &count)| count % 2 != 0)
            .map(|(&ch, _)| ch)
            .collect();
        if odd_chars.len() > 1 {
            return vec![];
        }
        let middle = if odd_chars.len() == 1 {
            String::from(odd_chars[0] as char)
        } else {
            String::new()
        };

        let mut keys: Vec<u8> = counts.keys().copied().collect();
        keys.sort_unstable();
        let mut half = Vec::new();
        for key in keys {
            for _ in 0..counts[&key] / 2 {
                half.push(key);
            }
        }

        let mut result = Vec::new();
        let mut used = vec![false; half.len()];
        let mut path = Vec::new();

        fn backtrack(
            half: &[u8],
            used: &mut [bool],
            path: &mut Vec<u8>,
            middle: &str,
            result: &mut Vec<String>,
        ) {
            if path.len() == half.len() {
                let prefix = String::from_utf8(path.clone()).unwrap();
                let reversed: String = prefix.chars().rev().collect();
                result.push(format!("{prefix}{middle}{reversed}"));
                return;
            }
            for index in 0..half.len() {
                if used[index] {
                    continue;
                }
                if index > 0 && half[index] == half[index - 1] && !used[index - 1] {
                    continue;
                }
                used[index] = true;
                path.push(half[index]);
                backtrack(half, used, path, middle, result);
                path.pop();
                used[index] = false;
            }
        }

        backtrack(&half, &mut used, &mut path, &middle, &mut result);
        result
    }
}
