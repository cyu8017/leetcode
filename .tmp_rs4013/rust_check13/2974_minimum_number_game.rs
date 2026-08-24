#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

impl Solution {
    pub fn number_game(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort_unstable();
        let mut i = 0;
        while i + 1 < nums.len() {
            nums.swap(i, i + 1);
            i += 2;
        }
        nums
    }
}
