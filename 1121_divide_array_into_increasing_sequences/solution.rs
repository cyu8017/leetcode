// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

use std::collections::HashMap;

impl Solution {
    pub fn can_divide_into_subsequences(nums: Vec<i32>, k: i32) -> bool {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        let mut max_freq = 0;
        for x in &nums {
            let e = freq.entry(*x).or_insert(0);
            *e += 1;
            max_freq = max_freq.max(*e);
        }
        nums.len() as i32 >= k * max_freq
    }
}
