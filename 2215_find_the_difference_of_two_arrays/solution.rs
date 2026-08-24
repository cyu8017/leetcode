// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

use std::collections::HashSet;

impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let s1: HashSet<i32> = nums1.into_iter().collect();
        let s2: HashSet<i32> = nums2.into_iter().collect();
        let a: Vec<i32> = s1.iter().copied().filter(|x| !s2.contains(x)).collect();
        let b: Vec<i32> = s2.iter().copied().filter(|x| !s1.contains(x)).collect();
        vec![a, b]
    }
}
