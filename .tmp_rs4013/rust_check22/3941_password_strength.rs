struct Solution;
// LeetCode 3941 - Password Strength
// https://leetcode.com/problems/password-strength/

use std::collections::HashSet;

impl Solution {
    pub fn password_strength(password: String) -> i32 {
        let st: HashSet<char> = password.chars().collect();
        let mut ans = 0;
        for ch in st {
            if ch.is_ascii_lowercase() {
                ans += 1;
            } else if ch.is_ascii_uppercase() {
                ans += 2;
            } else if ch.is_ascii_digit() {
                ans += 3;
            } else {
                ans += 5;
            }
        }
        ans
    }
}

fn main() {}
