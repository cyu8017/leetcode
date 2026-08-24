// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_cost(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2];
            g[u].push((v, w));
            g[v].push((u, w * 2));
        }
        let inf = i32::MAX / 2;
        let mut dist = vec![inf; n];
        dist[0] = 0;
        let mut pq: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        pq.push(Reverse((0, 0)));
        while let Some(Reverse((d, u))) = pq.pop() {
            if d > dist[u] {
                continue;
            }
            if u == n - 1 {
                return d;
            }
            for &(v, w) in &g[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    pq.push(Reverse((nd, v)));
                }
            }
        }
        -1
    }
}
