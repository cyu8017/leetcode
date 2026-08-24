// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_time(n: i32, edges: Vec<Vec<i32>>, disappear: Vec<i32>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        const INF: i32 = 1 << 30;
        let mut dist = vec![INF; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i32, 0usize)));
        while let Some(Reverse((du, u))) = pq.pop() {
            if du > dist[u] {
                continue;
            }
            for &(v, w) in &g[u] {
                if dist[v] > dist[u] + w && dist[u] + w < disappear[v] {
                    dist[v] = dist[u] + w;
                    pq.push(Reverse((dist[v], v)));
                }
            }
        }
        (0..n).map(|i| if dist[i] < disappear[i] { dist[i] } else { -1 }).collect()
    }
}
