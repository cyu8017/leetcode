#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

impl Solution {
    pub fn find_peaks(mountain: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 1..mountain.len().saturating_sub(1) {
            if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1] {
                ans.push(i as i32);
            }
        }
        ans
    }
}
