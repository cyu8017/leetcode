#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

impl Solution {
    pub fn return_to_boundary_count(nums: Vec<i32>) -> i32 {
        let mut s = 0;
        let mut ans = 0;
        for x in nums {
            s += x;
            if s == 0 {
                ans += 1;
            }
        }
        ans
    }
}
