// LeetCode 0349 - Intersection of Two Arrays
// https://leetcode.com/problems/intersection-of-two-arrays/

use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let set1: HashSet<i32> = nums1.into_iter().collect();
        let set2: HashSet<i32> = nums2.into_iter().collect();

        set1.into_iter()
            .filter(|value| set2.contains(value))
            .collect()
    }
}
