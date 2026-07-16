// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn remove_invalid_parentheses(s: String) -> Vec<String> {
        fn is_valid(text: &str) -> bool {
            let mut balance = 0;
            for character in text.chars() {
                match character {
                    '(' => balance += 1,
                    ')' => {
                        if balance == 0 {
                            return false;
                        }
                        balance -= 1;
                    }
                    _ => {}
                }
            }
            balance == 0
        }

        let mut result: HashSet<String> = HashSet::new();
        let mut queue = VecDeque::from([s.clone()]);
        let mut visited: HashSet<String> = HashSet::from([s.clone()]);
        let mut found = false;

        while !queue.is_empty() {
            let level_size = queue.len();
            for _ in 0..level_size {
                let current = queue.pop_front().unwrap();
                if is_valid(&current) {
                    result.insert(current.clone());
                    found = true;
                }
                if found {
                    continue;
                }
                let bytes: Vec<char> = current.chars().collect();
                for index in 0..bytes.len() {
                    if bytes[index] != '(' && bytes[index] != ')' {
                        continue;
                    }
                    let next: String = bytes
                        .iter()
                        .enumerate()
                        .filter(|(position, _)| *position != index)
                        .map(|(_, character)| *character)
                        .collect();
                    if visited.insert(next.clone()) {
                        queue.push_back(next);
                    }
                }
            }
        }

        result.into_iter().collect()
    }
}
