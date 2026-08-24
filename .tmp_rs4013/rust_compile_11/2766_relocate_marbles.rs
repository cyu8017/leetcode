struct Solution;
fn main() {}

// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

use std::collections::HashSet;

impl Solution {
    pub fn relocate_marbles(nums: Vec<i32>, move_from: Vec<i32>, move_to: Vec<i32>) -> Vec<i32> {
        let mut pos: HashSet<i32> = nums.into_iter().collect();
        for i in 0..move_from.len() {
            pos.remove(&move_from[i]);
            pos.insert(move_to[i]);
        }
        let mut ans: Vec<i32> = pos.into_iter().collect();
        ans.sort_unstable();
        ans
    }
}
