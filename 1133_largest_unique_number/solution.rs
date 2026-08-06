// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

use std::collections::HashMap;

impl Solution {
    pub fn largest_unique_number(nums: Vec<i32>) -> i32 {
        let mut count = HashMap::new();
        for x in nums {
            *count.entry(x).or_insert(0) += 1;
        }
        let mut ans = -1;
        for (x, c) in count {
            if c == 1 && x > ans {
                ans = x;
            }
        }
        ans
    }
}
