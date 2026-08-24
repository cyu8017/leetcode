#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3024 - Type of Triangle
// https://leetcode.com/problems/type-of-triangle/

impl Solution {
    pub fn triangle_type(mut nums: Vec<i32>) -> String {
        nums.sort_unstable();
        if nums[0] + nums[1] <= nums[2] {
            return "none".to_string();
        }
        if nums[0] == nums[2] {
            return "equilateral".to_string();
        }
        if nums[0] == nums[1] || nums[1] == nums[2] {
            return "isosceles".to_string();
        }
        "scalene".to_string()
    }
}
