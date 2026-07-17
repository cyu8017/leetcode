// LeetCode 1752 - Check if Array Is Sorted and Rotated
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let drops = (0..n).filter(|&i| nums[i] > nums[(i + 1) % n]).count();
        drops <= 1
    }
}
