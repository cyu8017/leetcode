// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut ops = 0;
        for i in (0..nums.len() - 1).rev() {
            if nums[i] != nums[i + 1] {
                ops += 1;
            }
        }
        ops
    }
}
