// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

impl Solution {
    pub fn min_moves(nums: Vec<i32>) -> i32 {
        let minimum = *nums.iter().min().unwrap();
        nums.iter().map(|value| value - minimum).sum()
    }
}
