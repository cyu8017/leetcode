// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn minimum_jumps(forbidden: Vec<i32>, a: i32, b: i32, x: i32) -> i32 {
        let bad: HashSet<i32> = forbidden.iter().copied().collect();
        let limit = x.max(*forbidden.iter().max().unwrap_or(&0)) + a + b;
        let mut q = VecDeque::from([(0i32, 0i32, false)]);
        let mut seen = HashSet::from([(0i32, false)]);
        while let Some((p, d, back)) = q.pop_front() {
            if p == x {
                return d;
            }
            for (np, nb) in [(p + a, false), (p - b, true)] {
                if np >= 0
                    && np <= limit
                    && !bad.contains(&np)
                    && seen.insert((np, nb))
                    && !(back && nb)
                {
                    q.push_back((np, d + 1, nb));
                }
            }
        }
        -1
    }
}
