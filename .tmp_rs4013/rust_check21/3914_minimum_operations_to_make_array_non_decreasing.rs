struct Solution;
// LeetCode 3914 - Minimum Operations to Make Array Non-Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        for i in 1..nums.len() {
            ans += 0.max(nums[i - 1] as i64 - nums[i] as i64);
        }
        ans
    }
}
