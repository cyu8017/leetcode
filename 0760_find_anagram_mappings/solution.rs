// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn anagram_mappings(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut positions: HashMap<i32, VecDeque<i32>> = HashMap::new();
        for (i, &value) in nums2.iter().enumerate() {
            positions.entry(value).or_default().push_back(i as i32);
        }
        nums1
            .into_iter()
            .map(|value| positions.get_mut(&value).unwrap().pop_front().unwrap())
            .collect()
    }
}
