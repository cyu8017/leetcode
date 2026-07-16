// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

use std::collections::HashMap;

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut next_greater = HashMap::new();
        let mut stack = Vec::new();
        for num in nums2 {
            while stack.last().copied().unwrap_or(i32::MIN) < num {
                next_greater.insert(stack.pop().unwrap(), num);
            }
            stack.push(num);
        }
        nums1
            .into_iter()
            .map(|num| *next_greater.get(&num).unwrap_or(&-1))
            .collect()
    }
}
