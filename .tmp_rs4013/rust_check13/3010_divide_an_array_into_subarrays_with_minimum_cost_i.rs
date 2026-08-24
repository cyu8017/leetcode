#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        let a = nums[0];
        let mut b = 100;
        let mut c = 100;
        for &x in nums.iter().skip(1) {
            if x < b {
                c = b;
                b = x;
            } else if x < c {
                c = x;
            }
        }
        a + b + c
    }
}
