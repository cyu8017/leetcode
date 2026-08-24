#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

impl Solution {
    pub fn divide_array(mut nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let mut ans = Vec::new();
        let mut i = 0;
        while i < nums.len() {
            if nums[i + 2] - nums[i] > k {
                return vec![];
            }
            ans.push(vec![nums[i], nums[i + 1], nums[i + 2]]);
            i += 3;
        }
        ans
    }
}
