// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        if nums.iter().all(|&x| x == nums[0]) {
            0
        } else {
            1
        }
    }
}
