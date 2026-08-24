// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn shortest_path_with_hops(
        n: i32,
        edges: Vec<Vec<i32>>,
        s: i32,
        d: i32,
        k: i32,
    ) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        let mut dist = vec![vec![i32::MAX / 4; k + 1]; n];
        dist[s as usize][0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0, s as usize, 0usize)));
        while let Some(Reverse((cd, u, hops))) = pq.pop() {
            if u == d as usize {
                return cd;
            }
            if cd > dist[u][hops] {
                continue;
            }
            for &(to, w) in &g[u] {
                if cd + w < dist[to][hops] {
                    dist[to][hops] = cd + w;
                    pq.push(Reverse((dist[to][hops], to, hops)));
                }
                if hops < k && cd < dist[to][hops + 1] {
                    dist[to][hops + 1] = cd;
                    pq.push(Reverse((cd, to, hops + 1)));
                }
            }
        }
        -1
    }
}
