#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

use std::collections::HashSet;

impl Solution {
    pub fn find_intersection_values(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let s1: HashSet<i32> = nums1.iter().copied().collect();
        let s2: HashSet<i32> = nums2.iter().copied().collect();
        let a = nums1.iter().filter(|v| s2.contains(v)).count() as i32;
        let b = nums2.iter().filter(|v| s1.contains(v)).count() as i32;
        vec![a, b]
    }
}
