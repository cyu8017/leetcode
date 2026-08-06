// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn count_paths(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for r in &roads {
            let (u, v, t) = (r[0] as usize, r[1] as usize, r[2] as i64);
            g[u].push((v, t));
            g[v].push((u, t));
        }
        let mut dist = vec![i64::MAX; n];
        let mut ways = vec![0i64; n];
        dist[0] = 0;
        ways[0] = 1;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i64, 0usize)));
        while let Some(Reverse((d, u))) = pq.pop() {
            if d > dist[u] {
                continue;
            }
            for &(v, w) in &g[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    ways[v] = ways[u];
                    pq.push(Reverse((nd, v)));
                } else if nd == dist[v] {
                    ways[v] = (ways[v] + ways[u]) % MOD;
                }
            }
        }
        ways[n - 1] as i32
    }
}
