// LeetCode 1708 - Largest Subarray Length K
// https://leetcode.com/problems/largest-subarray-length-k/

impl Solution {
    pub fn largest_subarray(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut start = 0;
        for i in 1..=(nums.len() - k) {
            if nums[i] > nums[start] {
                start = i;
            }
        }
        nums[start..start + k].to_vec()
    }
}
