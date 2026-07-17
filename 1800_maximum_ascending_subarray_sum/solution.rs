// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let mut best = nums[0];
        let mut cur = nums[0];
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                cur += nums[i];
            } else {
                cur = nums[i];
            }
            best = best.max(cur);
        }
        best
    }
}
