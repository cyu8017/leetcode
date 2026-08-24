// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        nums.iter().filter(|&&x| x < k).count() as i32
    }
}
