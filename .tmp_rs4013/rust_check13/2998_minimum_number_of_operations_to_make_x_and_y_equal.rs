#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn minimum_operations_to_make_equal(x: i32, y: i32) -> i32 {
        if x <= y {
            return y - x;
        }
        let mut q = VecDeque::new();
        q.push_back((x, 0));
        let mut seen = HashSet::new();
        seen.insert(x);
        while let Some((v, d)) = q.pop_front() {
            if v == y {
                return d;
            }
            let mut cands = vec![v + 1, v - 1];
            if v % 11 == 0 {
                cands.push(v / 11);
            }
            if v % 5 == 0 {
                cands.push(v / 5);
            }
            for nxt in cands {
                if nxt > 0 && nxt < 2 * x + 20 && seen.insert(nxt) {
                    q.push_back((nxt, d + 1));
                }
            }
        }
        -1
    }
}
