// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn busiest_servers(k: i32, arrival: Vec<i32>, load: Vec<i32>) -> Vec<i32> {
        let k = k as usize;
        let mut free: BinaryHeap<Reverse<i32>> = (0..k as i32).map(Reverse).collect();
        let mut busy: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        let mut count = vec![0i32; k];
        for (i, (&t, &length)) in arrival.iter().zip(load.iter()).enumerate() {
            let i = i as i32;
            while let Some(&Reverse((end, server))) = busy.peek() {
                if end > t {
                    break;
                }
                busy.pop();
                free.push(Reverse(i + (server - i).rem_euclid(k as i32)));
            }
            if free.is_empty() {
                continue;
            }
            let server = (free.pop().unwrap().0 % k as i32) as usize;
            count[server] += 1;
            busy.push(Reverse((t + length, server as i32)));
        }
        let best = *count.iter().max().unwrap_or(&0);
        count
            .into_iter()
            .enumerate()
            .filter(|&(_, c)| c == best)
            .map(|(i, _)| i as i32)
            .collect()
    }
}
