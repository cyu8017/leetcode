struct Solution;
// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let mut start = 0;
        for i in 0..=n {
            if i == n || chars[i] == ' ' {
                chars[start..i].reverse();
                start = i + 1;
            }
        }
        chars.into_iter().collect()
    }
}

fn main() {}
