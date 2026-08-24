// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

use std::collections::HashSet;

impl Solution {
    pub fn validate_coupons(code: Vec<String>, business_line: Vec<String>, is_active: Vec<bool>) -> Vec<String> {
        let bs: HashSet<&str> = ["electronics", "grocery", "pharmacy", "restaurant"].into_iter().collect();
        let check = |s: &str| -> bool {
            if s.is_empty() {
                return false;
            }
            s.chars().all(|c| c.is_ascii_alphanumeric() || c == '_')
        };
        let mut idx: Vec<usize> = (0..code.len())
            .filter(|&i| is_active[i] && bs.contains(business_line[i].as_str()) && check(&code[i]))
            .collect();
        idx.sort_by(|&i, &j| {
            business_line[i]
                .cmp(&business_line[j])
                .then_with(|| code[i].cmp(&code[j]))
        });
        idx.into_iter().map(|i| code[i].clone()).collect()
    }
}
