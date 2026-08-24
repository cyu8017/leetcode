// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0; n];
        let mut i = 0;
        let mut j = n - 1;
        for k in (0..n).rev() {
            if nums[i].abs() > nums[j].abs() {
                ans[k] = nums[i] * nums[i];
                i += 1;
            } else {
                ans[k] = nums[j] * nums[j];
                j -= 1;
            }
        }
        ans
    }
}
