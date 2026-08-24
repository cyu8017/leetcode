// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

use std::collections::HashSet;

impl Solution {
    pub fn arithmetic_triplets(nums: Vec<i32>, diff: i32) -> i32 {
        let seen: HashSet<i32> = nums.iter().copied().collect();
        nums.iter()
            .filter(|&&x| seen.contains(&(x + diff)) && seen.contains(&(x + 2 * diff)))
            .count() as i32
    }
}
