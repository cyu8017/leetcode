#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

impl Solution {
    pub fn minimum_array_length(nums: Vec<i32>) -> i32 {
        let mi = *nums.iter().min().unwrap();
        let mut cnt = 0;
        for &x in &nums {
            if x % mi != 0 {
                return 1;
            }
            if x == mi {
                cnt += 1;
            }
        }
        (cnt + 1) / 2
    }
}
