// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let k = k as usize;
        let mut window: i64 = nums[..k].iter().map(|&x| x as i64).sum();
        let mut best = window;
        for i in k..nums.len() {
            window += nums[i] as i64 - nums[i - k] as i64;
            best = best.max(window);
        }
        best as f64 / k as f64
    }
}
