// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_time_max_power(
        n: i32,
        edges: Vec<Vec<i32>>,
        power: i32,
        cost: Vec<i32>,
        source: i32,
        target: i32,
    ) -> Vec<i64> {
        const INF: i64 = 1 << 62;
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
        }
        let mut dist = vec![vec![INF; (power + 1) as usize]; n];
        let mut pq: BinaryHeap<Reverse<(i64, i32, usize)>> = BinaryHeap::new();
        pq.push(Reverse((0, -power, source as usize)));
        dist[source as usize][power as usize] = 0;
        while let Some(Reverse((d, neg_p, u))) = pq.pop() {
            let mut p = -neg_p;
            if u == target as usize {
                return vec![d, p as i64];
            }
            if d > dist[u][p as usize] || p < cost[u] {
                continue;
            }
            p -= cost[u];
            for &(v, t) in &g[u] {
                let nd = d + t as i64;
                if nd < dist[v][p as usize] {
                    dist[v][p as usize] = nd;
                    pq.push(Reverse((nd, -p, v)));
                }
            }
        }
        vec![-1, -1]
    }
}
