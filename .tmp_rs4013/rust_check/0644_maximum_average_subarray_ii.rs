struct Solution;
// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/

impl Solution {
    fn can_reach(nums: &[i32], k: usize, mid: f64) -> bool {
        let mut prefix = 0.0;
        for i in 0..k {
            prefix += nums[i] as f64 - mid;
        }
        if prefix >= 0.0 {
            return true;
        }
        let mut prev = 0.0f64;
        let mut min_prev = 0.0f64;
        for i in k..nums.len() {
            prefix += nums[i] as f64 - mid;
            prev += nums[i - k] as f64 - mid;
            min_prev = min_prev.min(prev);
            if prefix - min_prev >= 0.0 {
                return true;
            }
        }
        false
    }

    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let mut left = *nums.iter().min().unwrap() as f64;
        let mut right = *nums.iter().max().unwrap() as f64;
        for _ in 0..80 {
            let mid = (left + right) / 2.0;
            if Self::can_reach(&nums, k as usize, mid) {
                left = mid;
            } else {
                right = mid;
            }
        }
        left
    }
}

fn main() {}
