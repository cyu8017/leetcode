// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

impl Solution {
    pub fn get_sum_absolute_differences(nums: Vec<i32>) -> Vec<i32> {
        let total: i32 = nums.iter().sum();
        let n = nums.len() as i32;
        let mut left = 0i32;
        let mut ans = Vec::with_capacity(nums.len());
        for (i, &x) in nums.iter().enumerate() {
            let i = i as i32;
            ans.push(x * i - left + (total - left - x) - x * (n - i - 1));
            left += x;
        }
        ans
    }
}
