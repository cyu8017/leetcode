// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::<(usize, i32, i32)>::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2], e[3]));
        }
        const INF: i64 = 1_000_000_000_000_000_000;
        let mut dist = vec![INF; n];
        dist[0] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i64, 0usize)));
        while let Some(Reverse((t, u))) = pq.pop() {
            if t != dist[u] {
                continue;
            }
            if u == n - 1 {
                return t as i32;
            }
            for &(to, start, end) in &g[u] {
                let mut nt = t;
                if nt > end as i64 {
                    continue;
                }
                if nt < start as i64 {
                    nt = start as i64;
                }
                nt += 1;
                if nt < dist[to] {
                    dist[to] = nt;
                    pq.push(Reverse((nt, to)));
                }
            }
        }
        if dist[n - 1] == INF { -1 } else { dist[n - 1] as i32 }
    }
}
