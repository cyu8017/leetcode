// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

use std::collections::BTreeMap;

impl Solution {
    pub fn count_of_atoms(formula: String) -> String {
        let chars: Vec<char> = formula.chars().collect();
        let mut stack: Vec<BTreeMap<String, i32>> = vec![BTreeMap::new()];
        let mut i = 0;
        let n = chars.len();
        while i < n {
            if chars[i] == '(' {
                stack.push(BTreeMap::new());
                i += 1;
            } else if chars[i] == ')' {
                i += 1;
                let start = i;
                while i < n && chars[i].is_ascii_digit() {
                    i += 1;
                }
                let mult: i32 = if start < i {
                    chars[start..i].iter().collect::<String>().parse().unwrap()
                } else {
                    1
                };
                let top = stack.pop().unwrap();
                let dest = stack.last_mut().unwrap();
                for (atom, count) in top {
                    *dest.entry(atom).or_insert(0) += count * mult;
                }
            } else {
                let start = i;
                i += 1;
                while i < n && chars[i].is_ascii_lowercase() {
                    i += 1;
                }
                let atom: String = chars[start..i].iter().collect();
                let start = i;
                while i < n && chars[i].is_ascii_digit() {
                    i += 1;
                }
                let count: i32 = if start < i {
                    chars[start..i].iter().collect::<String>().parse().unwrap()
                } else {
                    1
                };
                *stack.last_mut().unwrap().entry(atom).or_insert(0) += count;
            }
        }
        let mut result = String::new();
        for (atom, count) in stack.pop().unwrap() {
            result.push_str(&atom);
            if count > 1 {
                result.push_str(&count.to_string());
            }
        }
        result
    }
}
