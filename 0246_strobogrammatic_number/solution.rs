// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

use std::collections::HashMap;

impl Solution {
    pub fn is_strobogrammatic(num: String) -> bool {
        let mapping: HashMap<char, char> = [
            ('0', '0'),
            ('1', '1'),
            ('6', '9'),
            ('8', '8'),
            ('9', '6'),
        ]
        .into_iter()
        .collect();
        let chars: Vec<char> = num.chars().collect();
        let mut left = 0;
        let mut right = chars.len().saturating_sub(1);
        while left <= right {
            if mapping.get(&chars[left]) != Some(&chars[right]) {
                return false;
            }
            left += 1;
            right = right.saturating_sub(1);
        }
        true
    }
}
