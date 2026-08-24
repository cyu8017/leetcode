// LeetCode 3738 - Longest Non-Decreasing Subarray After Replacing at Most One Element
// https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut left = vec![1; n];
        let mut right = vec![1; n];
        for i in 1..n {
            if nums[i] >= nums[i - 1] {
                left[i] = left[i - 1] + 1;
            }
        }
        for i in (0..n.saturating_sub(1)).rev() {
            if nums[i] <= nums[i + 1] {
                right[i] = right[i + 1] + 1;
            }
        }
        let mut ans = *left.iter().max().unwrap_or(&0);
        for i in 0..n {
            let a = if i > 0 { left[i - 1] } else { 0 };
            let b = if i + 1 < n { right[i + 1] } else { 0 };
            if i > 0 && i + 1 < n && nums[i - 1] > nums[i + 1] {
                ans = ans.max(a + 1).max(b + 1);
            } else {
                ans = ans.max(a + b + 1);
            }
        }
        ans
    }
}
