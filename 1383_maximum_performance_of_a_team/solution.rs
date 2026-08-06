// LeetCode 1383 - Maximum Performance of a Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn max_performance(n: i32, speed: Vec<i32>, efficiency: Vec<i32>, k: i32) -> i32 {
        let mut people: Vec<(i32, i32)> = efficiency.into_iter().zip(speed).collect();
        people.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        let mut total: i64 = 0;
        let mut ans: i64 = 0;
        let k = k as usize;
        for (e, s) in people {
            heap.push(Reverse(s));
            total += s as i64;
            if heap.len() > k {
                total -= heap.pop().unwrap().0 as i64;
            }
            ans = ans.max(total * e as i64);
        }
        (ans % 1_000_000_007) as i32
    }
}
