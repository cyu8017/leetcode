// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let values: HashMap<char, i32> = [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]
        .into_iter()
        .collect();

        let mut total = 0;
        let mut prev = 0;
        for ch in s.chars().rev() {
            let curr = values[&ch];
            if curr < prev {
                total -= curr;
            } else {
                total += curr;
            }
            prev = curr;
        }

        total
    }
}
