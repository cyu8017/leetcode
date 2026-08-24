#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2972 - Count the Number of Incremovable Subarrays II
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

impl Solution {
    pub fn incremovable_subarray_count(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut left: i32 = 0;
        while (left as usize) + 1 < n && nums[left as usize] < nums[left as usize + 1] {
            left += 1;
        }
        if left as usize == n - 1 {
            return n as i64 * (n as i64 + 1) / 2;
        }
        let mut ans = left as i64 + 2;
        let mut right = n as i32 - 1;
        while right > 0 && (right as usize == n - 1 || nums[right as usize] < nums[right as usize + 1]) {
            while left >= 0 && nums[left as usize] >= nums[right as usize] {
                left -= 1;
            }
            ans += left as i64 + 2;
            right -= 1;
            if right > 0 && nums[right as usize] >= nums[right as usize + 1] {
                break;
            }
        }
        ans
    }
}
