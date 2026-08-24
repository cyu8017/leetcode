// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

use std::collections::BinaryHeap;

impl Solution {
    pub fn convert_array(nums: Vec<i32>) -> i32 {
        fn cost(arr: &[i32]) -> i32 {
            let mut h = BinaryHeap::new();
            let mut ans = 0;
            for &x in arr {
                if let Some(&top) = h.peek() {
                    if top > x {
                        ans += top - x;
                        h.pop();
                        h.push(x);
                    }
                }
                h.push(x);
            }
            ans
        }
        let rev: Vec<i32> = nums.iter().copied().rev().collect();
        cost(&nums).min(cost(&rev))
    }
}
