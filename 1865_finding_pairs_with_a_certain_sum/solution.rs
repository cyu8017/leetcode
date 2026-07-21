// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

use std::collections::HashMap;

pub struct FindSumPairs {
    nums1: Vec<i32>,
    nums2: Vec<i32>,
    counts: HashMap<i32, i32>,
}

impl FindSumPairs {
    pub fn new(nums1: Vec<i32>, nums2: Vec<i32>) -> Self {
        let mut counts = HashMap::new();
        for &num in &nums2 {
            *counts.entry(num).or_insert(0) += 1;
        }
        Self {
            nums1,
            nums2,
            counts,
        }
    }

    pub fn add(&mut self, index: i32, val: i32) {
        let index = index as usize;
        *self.counts.entry(self.nums2[index]).or_insert(0) -= 1;
        self.nums2[index] += val;
        *self.counts.entry(self.nums2[index]).or_insert(0) += 1;
    }

    pub fn count(&self, tot: i32) -> i32 {
        self.nums1
            .iter()
            .map(|&num| *self.counts.get(&(tot - num)).unwrap_or(&0))
            .sum()
    }
}
