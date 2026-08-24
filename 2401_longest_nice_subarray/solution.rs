// LeetCode 2401 - Longest Nice Subarray
// https://leetcode.com/problems/longest-nice-subarray/

impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let mut used = 0;
        let mut left = 0;
        let mut ans = 0;
        for right in 0..nums.len() {
            while used & nums[right] != 0 {
                used ^= nums[left];
                left += 1;
            }
            used |= nums[right];
            ans = ans.max((right - left + 1) as i32);
        }
        ans
    }
}
