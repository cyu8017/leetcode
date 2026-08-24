// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        let mut ans = 1;
        let mut t = 1;
        for i in 1..nums.len() {
            if nums[i - 1] < nums[i] {
                t += 1;
                ans = ans.max(t);
            } else {
                t = 1;
            }
        }
        t = 1;
        for i in 1..nums.len() {
            if nums[i - 1] > nums[i] {
                t += 1;
                ans = ans.max(t);
            } else {
                t = 1;
            }
        }
        ans
    }
}
