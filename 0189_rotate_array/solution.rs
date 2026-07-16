// LeetCode 0189 - Rotate Array
// https://leetcode.com/problems/rotate-array/

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let k = k as usize % nums.len();
        nums.reverse();
        nums[..k].reverse();
        nums[k..].reverse();
    }
}