// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

impl Solution {
    pub fn last(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            -1
        } else {
            *nums.last().unwrap()
        }
    }
}
