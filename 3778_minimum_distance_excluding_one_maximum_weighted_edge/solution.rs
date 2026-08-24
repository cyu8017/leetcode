// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_cost_excluding_max(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2];
            g[u].push((v, w));
            g[v].push((u, w));
        }
        const INF: i64 = 4_000_000_000_000_000_000;
        let mut dist = vec![[INF; 2]; n];
        dist[0][0] = 0;
        let mut pq: BinaryHeap<Reverse<(i64, usize, usize)>> = BinaryHeap::new();
        pq.push(Reverse((0, 0, 0)));
        while let Some(Reverse((cur, u, used))) = pq.pop() {
            if cur > dist[u][used] {
                continue;
            }
            if u == n - 1 && used == 1 {
                return cur;
            }
            for &(v, w) in &g[u] {
                let nxt = cur + w as i64;
                if nxt < dist[v][used] {
                    dist[v][used] = nxt;
                    pq.push(Reverse((nxt, v, used)));
                }
                if used == 0 {
                    let nxt = cur;
                    if nxt < dist[v][1] {
                        dist[v][1] = nxt;
                        pq.push(Reverse((nxt, v, 1)));
                    }
                }
            }
        }
        dist[n - 1][1]
    }
}
