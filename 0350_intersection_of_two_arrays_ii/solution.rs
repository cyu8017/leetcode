// LeetCode 0350 - Intersection of Two Arrays II
// https://leetcode.com/problems/intersection-of-two-arrays-ii/

use std::collections::HashMap;

impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for num in nums1 {
            *counts.entry(num).or_insert(0) += 1;
        }

        let mut result = Vec::new();
        for num in nums2 {
            if let Some(value) = counts.get_mut(&num) {
                if *value > 0 {
                    result.push(num);
                    *value -= 1;
                }
            }
        }

        result
    }
}
