// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_cost(max_time: i32, edges: Vec<Vec<i32>>, passing_fee: Vec<i32>) -> i32 {
        let n = passing_fee.len();
        let mut graph = vec![Vec::new(); n];
        for e in edges {
            let (u, v, t) = (e[0] as usize, e[1] as usize, e[2]);
            graph[u].push((v, t));
            graph[v].push((u, t));
        }

        let mut min_time = vec![max_time + 1; n];
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((passing_fee[0], 0i32, 0usize)));
        while let Some(Reverse((cost, time, u))) = pq.pop() {
            if time >= min_time[u] {
                continue;
            }
            min_time[u] = time;
            if u == n - 1 {
                return cost;
            }
            for &(v, dt) in &graph[u] {
                let nt = time + dt;
                if nt <= max_time && nt < min_time[v] {
                    pq.push(Reverse((cost + passing_fee[v], nt, v)));
                }
            }
        }
        -1
    }
}
