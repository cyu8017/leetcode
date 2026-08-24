// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

impl Solution {
    pub fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        if nums.len() <= 1 {
            return nums;
        }
        let mid = nums.len() / 2;
        let left = Self::sort_array(nums[..mid].to_vec());
        let right = Self::sort_array(nums[mid..].to_vec());
        let mut merged = Vec::with_capacity(nums.len());
        let mut i = 0;
        let mut j = 0;
        while i < left.len() && j < right.len() {
            if left[i] <= right[j] {
                merged.push(left[i]);
                i += 1;
            } else {
                merged.push(right[j]);
                j += 1;
            }
        }
        merged.extend_from_slice(&left[i..]);
        merged.extend_from_slice(&right[j..]);
        merged
    }
}
