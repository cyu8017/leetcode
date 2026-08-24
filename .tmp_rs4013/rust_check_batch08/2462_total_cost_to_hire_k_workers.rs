struct Solution;
// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn total_cost(costs: Vec<i32>, k: i32, candidates: i32) -> i64 {
        let n = costs.len();
        let candidates = candidates as usize;
        let mut left_h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut right_h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut l = 0usize;
        let mut r = n as i32 - 1;
        while l as i32 <= r && left_h.len() < candidates {
            left_h.push(Reverse((costs[l], l)));
            l += 1;
        }
        while r >= l as i32 && right_h.len() < candidates {
            right_h.push(Reverse((costs[r as usize], r as usize)));
            r -= 1;
        }
        let mut ans = 0i64;
        for _ in 0..k {
            let use_left = match (left_h.peek(), right_h.peek()) {
                (Some(Reverse((lv, li))), Some(Reverse((rv, ri)))) => {
                    *lv < *rv || (*lv == *rv && *li <= *ri)
                }
                (Some(_), None) => true,
                _ => false,
            };
            if use_left {
                let Reverse((v, _)) = left_h.pop().unwrap();
                ans += v as i64;
                if (l as i32) <= r {
                    left_h.push(Reverse((costs[l], l)));
                    l += 1;
                }
            } else {
                let Reverse((v, _)) = right_h.pop().unwrap();
                ans += v as i64;
                if (l as i32) <= r {
                    right_h.push(Reverse((costs[r as usize], r as usize)));
                    r -= 1;
                }
            }
        }
        ans
    }
}

fn main() {}
