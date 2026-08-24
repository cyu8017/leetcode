// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

impl Solution {
    pub fn valid_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut peaks = Vec::new();
        for i in 1..n.saturating_sub(1) {
            if nums[i] > nums[i - 1] && nums[i] > nums[i + 1] {
                peaks.push(i as i32);
            }
        }
        let mut ans = 0i64;
        for j in 0..peaks.len() {
            let p = peaks[j];
            let mut left_min = (p - k).max(0);
            if j > 0 {
                left_min = left_min.max(peaks[j - 1] + 1);
            }
            let mut right_max = (p + k).min(n as i32 - 1);
            if j + 1 < peaks.len() {
                right_max = right_max.min(peaks[j + 1] - 1);
            }
            ans += (p - left_min + 1) as i64 * (right_max - p + 1) as i64;
        }
        ans
    }
}
