// LeetCode 0336 - Palindrome Pairs
// https://leetcode.com/problems/palindrome-pairs/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn palindrome_pairs(words: Vec<String>) -> Vec<Vec<i32>> {
        let mut word_map: HashMap<&str, i32> = HashMap::new();
        for (index, word) in words.iter().enumerate() {
            word_map.insert(word.as_str(), index as i32);
        }

        let mut seen: HashSet<(i32, i32)> = HashSet::new();

        for (index, word) in words.iter().enumerate() {
            for split in 0..=word.len() {
                let (left, right) = word.split_at(split);
                if Self::is_palindrome(left) {
                    let reversed_right: String = right.chars().rev().collect();
                    if let Some(&other) = word_map.get(reversed_right.as_str()) {
                        if other as usize != index {
                            seen.insert((other, index as i32));
                        }
                    }
                }
                if Self::is_palindrome(right) {
                    let reversed_left: String = left.chars().rev().collect();
                    if let Some(&other) = word_map.get(reversed_left.as_str()) {
                        if other as usize != index {
                            seen.insert((index as i32, other));
                        }
                    }
                }
            }
        }

        seen.into_iter()
            .map(|(left, right)| vec![left, right])
            .collect()
    }

    fn is_palindrome(value: &str) -> bool {
        let bytes = value.as_bytes();
        let mut left = 0;
        let mut right = bytes.len();
        while left < right {
            right -= 1;
            if bytes[left] != bytes[right] {
                return false;
            }
            left += 1;
        }
        true
    }
}
