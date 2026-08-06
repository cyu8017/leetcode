// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

use std::collections::HashMap;

pub struct SparseVector {
    values: HashMap<usize, i32>,
}

impl SparseVector {
    pub fn new(nums: Vec<i32>) -> Self {
        let values = nums
            .into_iter()
            .enumerate()
            .filter(|&(_, x)| x != 0)
            .collect();
        Self { values }
    }

    pub fn dot_product(&self, vec: &SparseVector) -> i32 {
        if self.values.len() > vec.values.len() {
            return vec.dot_product(self);
        }
        self.values
            .iter()
            .map(|(&i, &x)| x * vec.values.get(&i).copied().unwrap_or(0))
            .sum()
    }
}

impl Solution {
    pub fn dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        SparseVector::new(nums1).dot_product(&SparseVector::new(nums2))
    }
}
