// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

impl Solution {
    pub fn three_sum_smaller(mut nums: Vec<i32>, target: i32) -> i32 {
        nums.sort_unstable();
        let mut count = 0;
        let length = nums.len();
        for index in 0..length.saturating_sub(2) {
            let mut left = index + 1;
            let mut right = length - 1;
            while left < right {
                let total = nums[index] + nums[left] + nums[right];
                if total < target {
                    count += (right - left) as i32;
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        count
    }
}
