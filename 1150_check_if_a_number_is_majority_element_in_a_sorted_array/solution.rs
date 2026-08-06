// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

impl Solution {
    pub fn is_majority_element(nums: Vec<i32>, target: i32) -> bool {
        let left = nums.partition_point(|&x| x < target);
        let right = nums.partition_point(|&x| x <= target);
        right - left > nums.len() / 2
    }
}
