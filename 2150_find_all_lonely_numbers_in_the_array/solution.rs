// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

use std::collections::HashMap;

impl Solution {
    pub fn find_lonely(nums: Vec<i32>) -> Vec<i32> {
        let mut freq = HashMap::new();
        for &x in &nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        freq.iter()
            .filter(|(&x, &c)| c == 1 && !freq.contains_key(&(x - 1)) && !freq.contains_key(&(x + 1)))
            .map(|(&x, _)| x)
            .collect()
    }
}
