#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

impl Solution {
    pub fn max_operations(nums: Vec<i32>) -> i32 {
        let s = nums[0] + nums[1];
        let n = nums.len();
        let mut ans = 0;
        let mut i = 0;
        while i + 1 < n && nums[i] + nums[i + 1] == s {
            ans += 1;
            i += 2;
        }
        ans
    }
}
