struct Solution;
// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

impl Solution {
    pub fn phone_prefix(mut numbers: Vec<String>) -> bool {
        numbers.sort();
        for i in 0..numbers.len().saturating_sub(1) {
            if numbers[i].len() <= numbers[i + 1].len() && numbers[i + 1].starts_with(&numbers[i]) {
                return false;
            }
        }
        true
    }
}

fn main() {}
