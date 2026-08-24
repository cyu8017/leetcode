// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

impl Solution {
    pub fn minimum_average_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let total: i64 = nums.iter().map(|&v| v as i64).sum();
        let mut left = 0i64;
        let mut best_diff = i64::MAX;
        let mut best_idx = 0;
        for i in 0..n {
            left += nums[i] as i64;
            let left_avg = left / (i as i64 + 1);
            let right_avg = if i != n - 1 {
                (total - left) / (n as i64 - i as i64 - 1)
            } else {
                0
            };
            let diff = (left_avg - right_avg).abs();
            if diff < best_diff {
                best_diff = diff;
                best_idx = i;
            }
        }
        best_idx as i32
    }
}
