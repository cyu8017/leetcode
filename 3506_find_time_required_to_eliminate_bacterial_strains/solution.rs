// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn min_elimination_time(time_req: Vec<i32>, split_time: i32) -> i64 {
        let mut pq: BinaryHeap<Reverse<i32>> = time_req.into_iter().map(Reverse).collect();
        while pq.len() > 1 {
            pq.pop();
            let Reverse(x) = pq.pop().unwrap();
            pq.push(Reverse(x + split_time));
        }
        pq.peek().unwrap().0 as i64
    }
}
