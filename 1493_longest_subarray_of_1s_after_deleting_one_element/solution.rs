// LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let mut left = 0usize;
        let mut zeros = 0;
        let mut ans = 0;
        for (right, &x) in nums.iter().enumerate() {
            zeros += i32::from(x == 0);
            while zeros > 1 {
                zeros -= i32::from(nums[left] == 0);
                left += 1;
            }
            ans = ans.max(right - left);
        }
        ans as i32
    }
}
