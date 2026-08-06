// LeetCode 1439 - Find the Kth Smallest Sum of a Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

use std::collections::{BinaryHeap, HashSet};
use std::cmp::Reverse;

impl Solution {
    pub fn kth_smallest(mat: Vec<Vec<i32>>, k: i32) -> i32 {
        let k = k as usize;
        let mut sums = vec![0];
        for row in mat {
            let mut heap = BinaryHeap::new();
            heap.push(Reverse((sums[0] + row[0], 0usize, 0usize)));
            let mut merged = Vec::new();
            let mut seen = HashSet::new();
            seen.insert((0usize, 0usize));
            while let Some(Reverse((value, i, j))) = heap.pop() {
                merged.push(value);
                if merged.len() == k {
                    break;
                }
                if j + 1 < row.len() && seen.insert((i, j + 1)) {
                    heap.push(Reverse((sums[i] + row[j + 1], i, j + 1)));
                }
                if j == 0 && i + 1 < sums.len() && seen.insert((i + 1, 0)) {
                    heap.push(Reverse((sums[i + 1] + row[0], i + 1, 0)));
                }
            }
            sums = merged;
        }
        sums[k - 1]
    }
}
