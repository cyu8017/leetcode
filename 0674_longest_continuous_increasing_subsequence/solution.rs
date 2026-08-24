// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        let mut best = 1;
        let mut cur = 1;
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                cur += 1;
                best = best.max(cur);
            } else {
                cur = 1;
            }
        }
        best
    }
}
