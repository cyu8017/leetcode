// LeetCode 3818 - Minimum Prefix Removal To Make Array Strictly Increasing
// https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

impl Solution {
    pub fn minimum_prefix_length(nums: Vec<i32>) -> i32 {
        for i in (1..nums.len()).rev() {
            if nums[i - 1] >= nums[i] {
                return i as i32;
            }
        }
        0
    }
}
