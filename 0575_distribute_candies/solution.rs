// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

use std::collections::HashSet;

impl Solution {
    pub fn distribute_candies(candy_type: Vec<i32>) -> i32 {
        let unique: HashSet<i32> = candy_type.iter().copied().collect();
        unique.len().min(candy_type.len() / 2) as i32
    }
}
