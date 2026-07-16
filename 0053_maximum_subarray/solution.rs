// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut best = nums[0];
        let mut current = nums[0];

        for i in 1..nums.len() {
            current = nums[i].max(current + nums[i]);
            best = best.max(current);
        }

        best
    }
}
