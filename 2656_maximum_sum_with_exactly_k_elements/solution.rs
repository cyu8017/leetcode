// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

impl Solution {
    pub fn maximize_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mx = *nums.iter().max().unwrap();
        k * mx + k * (k - 1) / 2
    }
}
