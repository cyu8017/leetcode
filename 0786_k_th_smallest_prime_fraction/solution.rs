// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn kth_smallest_prime_fraction(arr: Vec<i32>, k: i32) -> Vec<i32> {
        let n = arr.len();
        let mut heap = BinaryHeap::new();
        for i in 0..n - 1 {
            let frac = arr[i] as f64 / arr[n - 1] as f64;
            heap.push(Reverse((OrderedF64(frac), i, n - 1)));
        }
        for _ in 0..k - 1 {
            let Reverse((_, i, j)) = heap.pop().unwrap();
            if j - 1 > i {
                let frac = arr[i] as f64 / arr[j - 1] as f64;
                heap.push(Reverse((OrderedF64(frac), i, j - 1)));
            }
        }
        let Reverse((_, i, j)) = heap.pop().unwrap();
        vec![arr[i], arr[j]]
    }
}

#[derive(Copy, Clone, PartialEq)]
struct OrderedF64(f64);

impl Eq for OrderedF64 {}

impl PartialOrd for OrderedF64 {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for OrderedF64 {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.0.partial_cmp(&other.0).unwrap_or(std::cmp::Ordering::Equal)
    }
}
