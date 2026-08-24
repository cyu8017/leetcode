// LeetCode 2208 - Minimum Operations to Halve Array Sum
// https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

use std::collections::BinaryHeap;

impl Solution {
    pub fn halve_array(nums: Vec<i32>) -> i32 {
        let mut h = BinaryHeap::new();
        let mut sum = 0.0f64;
        for x in nums {
            h.push(ordered_float(x as f64));
            sum += x as f64;
        }
        let target = sum / 2.0;
        let mut ans = 0;
        while sum > target {
            let x = h.pop().unwrap().0 / 2.0;
            sum -= x;
            h.push(ordered_float(x));
            ans += 1;
        }
        ans
    }
}

#[derive(Copy, Clone, PartialEq, PartialOrd)]
struct F64(f64);

impl Eq for F64 {}
impl Ord for F64 {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.0.partial_cmp(&other.0).unwrap_or(std::cmp::Ordering::Equal)
    }
}

fn ordered_float(x: f64) -> F64 {
    F64(x)
}
