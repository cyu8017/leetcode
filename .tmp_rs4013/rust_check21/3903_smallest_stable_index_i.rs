struct Solution;
// LeetCode 3903 - Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/

impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut right = vec![0; n];
        right[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            right[i] = right[i + 1].min(nums[i]);
        }
        let mut left = 0;
        for i in 0..n {
            left = left.max(nums[i]);
            if left - right[i] <= k {
                return i as i32;
            }
        }
        -1
    }
}
