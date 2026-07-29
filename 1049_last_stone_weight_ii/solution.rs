// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

use std::collections::HashSet;

impl Solution {
    pub fn last_stone_weight_ii(stones: Vec<i32>) -> i32 {
        let total: i32 = stones.iter().sum();
        let mut reachable = HashSet::new();
        reachable.insert(0);
        for stone in stones {
            let mut next = HashSet::new();
            for &s in &reachable {
                next.insert(s + stone);
                next.insert(s);
            }
            reachable = next;
        }
        reachable
            .into_iter()
            .map(|s| (total - 2 * s).abs())
            .min()
            .unwrap()
    }
}
