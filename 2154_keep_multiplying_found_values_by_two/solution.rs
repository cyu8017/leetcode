// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

use std::collections::HashSet;

impl Solution {
    pub fn find_final_value(nums: Vec<i32>, mut original: i32) -> i32 {
        let have: HashSet<i32> = nums.into_iter().collect();
        while have.contains(&original) {
            original *= 2;
        }
        original
    }
}
