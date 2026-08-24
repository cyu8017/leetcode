// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

use std::collections::HashMap;

impl Solution {
    pub fn once_twice(nums: Vec<i32>) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut a = 0;
        let mut b = 0;
        for (&x, &c) in &freq {
            if c == 1 {
                a = x;
            } else if c == 2 {
                b = x;
            }
        }
        vec![a, b]
    }
}
