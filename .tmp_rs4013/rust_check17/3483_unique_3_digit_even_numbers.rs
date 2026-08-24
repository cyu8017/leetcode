struct Solution;
// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

use std::collections::HashSet;

impl Solution {
    pub fn total_numbers(digits: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        let n = digits.len();
        for i in 0..n {
            for j in 0..n {
                if j == i {
                    continue;
                }
                for k in 0..n {
                    if k == i || k == j {
                        continue;
                    }
                    if digits[i] == 0 {
                        continue;
                    }
                    if digits[k] % 2 != 0 {
                        continue;
                    }
                    seen.insert(digits[i] * 100 + digits[j] * 10 + digits[k]);
                }
            }
        }
        seen.len() as i32
    }
}

fn main() {}
