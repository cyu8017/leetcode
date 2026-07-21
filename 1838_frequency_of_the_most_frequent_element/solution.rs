// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut left = 0usize;
        let mut window_sum: i64 = 0;
        let mut best = 0i32;

        for right in 0..nums.len() {
            let value = nums[right] as i64;
            window_sum += value;
            while value * (right as i64 - left as i64 + 1) - window_sum > k as i64 {
                window_sum -= nums[left] as i64;
                left += 1;
            }
            best = best.max((right - left + 1) as i32);
        }

        best
    }
}
