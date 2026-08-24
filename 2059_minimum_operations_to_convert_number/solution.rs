// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>, start: i32, goal: i32) -> i32 {
        if start == goal {
            return 0;
        }
        let mut vis = HashSet::new();
        vis.insert(start);
        let mut q = VecDeque::new();
        q.push_back(start);
        let mut steps = 0;
        while !q.is_empty() {
            steps += 1;
            let sz = q.len();
            for _ in 0..sz {
                let cur = q.pop_front().unwrap();
                for &x in &nums {
                    for nxt in [cur + x, cur - x, cur ^ x] {
                        if nxt == goal {
                            return steps;
                        }
                        if nxt >= 0 && nxt <= 1000 && vis.insert(nxt) {
                            q.push_back(nxt);
                        }
                    }
                }
            }
        }
        -1
    }
}
