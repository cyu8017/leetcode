// LeetCode 0462 - Minimum Moves to Equal Array Elements II
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

impl Solution {
    pub fn min_moves2(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let median = nums[nums.len() / 2];
        nums.iter().map(|value| (value - median).abs()).sum()
    }
}
