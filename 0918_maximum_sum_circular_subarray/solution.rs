// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

impl Solution {
    pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
        let total: i32 = nums.iter().sum();
        let mut max_sum = nums[0];
        let mut min_sum = nums[0];
        let mut cur_max = nums[0];
        let mut cur_min = nums[0];
        for &x in nums.iter().skip(1) {
            cur_max = x.max(cur_max + x);
            cur_min = x.min(cur_min + x);
            max_sum = max_sum.max(cur_max);
            min_sum = min_sum.min(cur_min);
        }
        if max_sum < 0 {
            return max_sum;
        }
        max_sum.max(total - min_sum)
    }
}
