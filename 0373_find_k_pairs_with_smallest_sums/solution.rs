// LeetCode 0373 - Find K Pairs with Smallest Sums
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        if nums1.is_empty() || nums2.is_empty() || k == 0 {
            return Vec::new();
        }

        let k = k as usize;
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        let seed_count = nums1.len().min(k);

        for index in 0..seed_count {
            heap.push(Reverse((nums1[index] + nums2[0], index, 0)));
        }

        let mut result = Vec::new();
        while let Some(Reverse((_, index1, index2))) = heap.pop() {
            result.push(vec![nums1[index1], nums2[index2]]);
            if result.len() == k {
                break;
            }
            if index2 + 1 < nums2.len() {
                heap.push(Reverse((nums1[index1] + nums2[index2 + 1], index1, index2 + 1)));
            }
        }

        result
    }
}
