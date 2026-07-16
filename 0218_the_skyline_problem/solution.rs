// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn get_skyline(buildings: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut events: Vec<(i32, i32, i32)> = Vec::new();
        for building in buildings {
            events.push((building[0], -building[2], building[1]));
            events.push((building[1], 0, 0));
        }
        events.sort_by(|a, b| a.0.cmp(&b.0).then(a.1.cmp(&b.1)));

        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut live: BinaryHeap<(Reverse<i32>, i32)> = BinaryHeap::new();
        live.push((Reverse(0), i32::MAX));

        for (x, neg_h, end) in events {
            while live.peek().map_or(false, |item| item.1 <= x) {
                live.pop();
            }
            if neg_h != 0 {
                live.push((Reverse(neg_h), end));
            }
            let height = -live.peek().unwrap().0.0;
            if result.is_empty() || result.last().unwrap()[1] != height {
                result.push(vec![x, height]);
            }
        }
        result
    }
}
