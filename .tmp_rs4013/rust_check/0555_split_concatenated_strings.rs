struct Solution;
// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

impl Solution {
    pub fn split_looped_string(strs: Vec<String>) -> String {
        let best_forms: Vec<String> = strs
            .iter()
            .map(|s| {
                let rev: String = s.chars().rev().collect();
                if s.as_str() > rev.as_str() {
                    s.clone()
                } else {
                    rev
                }
            })
            .collect();

        let mut answer = String::new();
        for i in 0..strs.len() {
            let mut mid = String::new();
            for j in i + 1..strs.len() {
                mid.push_str(&best_forms[j]);
            }
            for j in 0..i {
                mid.push_str(&best_forms[j]);
            }
            let original = &strs[i];
            let reversed: String = original.chars().rev().collect();
            for candidate in [original.as_str(), reversed.as_str()] {
                let chars: Vec<char> = candidate.chars().collect();
                for cut in 0..chars.len() {
                    let formed: String = chars[cut..]
                        .iter()
                        .copied()
                        .chain(mid.chars())
                        .chain(chars[..cut].iter().copied())
                        .collect();
                    if formed > answer {
                        answer = formed;
                    }
                }
            }
        }
        answer
    }
}

fn main() {}
