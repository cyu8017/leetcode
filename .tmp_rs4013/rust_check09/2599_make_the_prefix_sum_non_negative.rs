struct Solution;

// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn make_pref_sum_non_negative(nums: Vec<i32>) -> i32 {
        let mut h: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut sum = 0i64;
        let mut ans = 0;
        for x in nums {
            sum += x as i64;
            if x < 0 {
                h.push(Reverse(x));
            }
            if sum < 0 {
                let worst = h.pop().unwrap().0;
                sum -= worst as i64;
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
