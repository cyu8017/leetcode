// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

impl Solution {
    pub fn max_absolute_sum(nums: Vec<i32>) -> i32 {
        let mut prefix = 0;
        let mut low = 0;
        let mut high = 0;
        for &value in &nums {
            prefix += value;
            low = low.min(prefix);
            high = high.max(prefix);
        }
        high - low
    }
}
