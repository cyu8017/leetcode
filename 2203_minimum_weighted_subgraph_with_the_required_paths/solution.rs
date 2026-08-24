// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    fn dijkstra(n: usize, g: &[Vec<(usize, i32)>], src: usize) -> Vec<i64> {
        const INF: i64 = 1i64 << 62;
        let mut dist = vec![INF; n];
        dist[src] = 0;
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0i64, src)));
        while let Some(Reverse((d, u))) = pq.pop() {
            if d != dist[u] {
                continue;
            }
            for &(v, w) in &g[u] {
                if d + w as i64 < dist[v] {
                    dist[v] = d + w as i64;
                    pq.push(Reverse((dist[v], v)));
                }
            }
        }
        dist
    }

    pub fn minimum_weight(n: i32, edges: Vec<Vec<i32>>, src1: i32, src2: i32, dest: i32) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        let mut rg = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            rg[e[1] as usize].push((e[0] as usize, e[2]));
        }
        let d1 = Self::dijkstra(n, &g, src1 as usize);
        let d2 = Self::dijkstra(n, &g, src2 as usize);
        let dd = Self::dijkstra(n, &rg, dest as usize);
        const INF: i64 = 1i64 << 62;
        let mut ans = INF;
        for i in 0..n {
            if d1[i] >= INF || d2[i] >= INF || dd[i] >= INF {
                continue;
            }
            ans = ans.min(d1[i] + d2[i] + dd[i]);
        }
        if ans >= INF { -1 } else { ans }
    }
}
