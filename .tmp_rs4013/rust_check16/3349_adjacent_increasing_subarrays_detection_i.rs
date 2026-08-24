struct Solution;
// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

impl Solution {
    pub fn has_increasing_subarrays(nums: Vec<i32>, k: i32) -> bool {
        let n = nums.len();
        let k = k as usize;
        let inc = |start: usize| -> bool {
            for i in start..start + k - 1 {
                if nums[i] >= nums[i + 1] {
                    return false;
                }
            }
            true
        };
        let mut i = 0;
        while i + 2 * k <= n {
            if inc(i) && inc(i + k) {
                return true;
            }
            i += 1;
        }
        false
    }
}

fn main() {}
