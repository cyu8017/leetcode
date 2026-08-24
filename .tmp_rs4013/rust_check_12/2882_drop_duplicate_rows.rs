struct Solution;
// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/

use std::collections::HashSet;

impl Solution {
    pub fn drop_duplicate_emails(customers: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut seen = HashSet::new();
        let mut out = Vec::new();
        for r in customers {
            let email = *r.last().unwrap_or(&0);
            if seen.insert(email) {
                out.push(r);
            }
        }
        out
    }
}

fn main() {}
