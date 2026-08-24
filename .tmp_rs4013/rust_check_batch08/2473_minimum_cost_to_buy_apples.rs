struct Solution;
// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_cost(n: i32, roads: Vec<Vec<i32>>, apple_cost: Vec<i32>, k: i32) -> Vec<i64> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for r in &roads {
            let (a, b, w) = (r[0] as usize, r[1] as usize, r[2] as i64);
            g[a].push((b, w));
            g[b].push((a, w));
        }
        let mut ans = vec![0i64; n];
        const INF: i64 = 1 << 60;
        for start in 1..=n {
            let mut dist = vec![INF; n + 1];
            dist[start] = 0;
            let mut pq: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
            pq.push(Reverse((0, start)));
            while let Some(Reverse((d, u))) = pq.pop() {
                if d != dist[u] {
                    continue;
                }
                for &(v, w) in &g[u] {
                    let nd = d + w;
                    if nd < dist[v] {
                        dist[v] = nd;
                        pq.push(Reverse((nd, v)));
                    }
                }
            }
            let mut best = INF;
            for city in 1..=n {
                let cost = dist[city] * (k as i64 + 1) + apple_cost[city - 1] as i64;
                if cost < best {
                    best = cost;
                }
            }
            ans[start - 1] = best;
        }
        ans
    }
}

fn main() {}
