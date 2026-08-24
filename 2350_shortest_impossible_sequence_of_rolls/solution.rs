// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

use std::collections::HashSet;

impl Solution {
    pub fn shortest_sequence(rolls: Vec<i32>, k: i32) -> i32 {
        let mut seen = HashSet::new();
        let mut ans = 1;
        for r in rolls {
            seen.insert(r);
            if seen.len() as i32 == k {
                ans += 1;
                seen.clear();
            }
        }
        ans
    }
}
