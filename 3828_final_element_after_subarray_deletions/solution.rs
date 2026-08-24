// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

impl Solution {
    pub fn final_element(nums: Vec<i32>) -> i32 {
        *nums.first().unwrap().max(nums.last().unwrap())
    }
}
