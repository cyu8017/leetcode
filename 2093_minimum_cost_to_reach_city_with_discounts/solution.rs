// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_cost(n: i32, highways: Vec<Vec<i32>>, discounts: i32) -> i32 {
        let n = n as usize;
        let discounts = discounts as usize;
        let mut g = vec![Vec::new(); n];
        for h in highways {
            let (a, b, w) = (h[0] as usize, h[1] as usize, h[2]);
            g[a].push((b, w));
            g[b].push((a, w));
        }
        const INF: i32 = 1 << 30;
        let mut dist = vec![vec![INF; discounts + 1]; n];
        let mut pq = BinaryHeap::new();
        dist[0][discounts] = 0;
        pq.push(Reverse((0, 0usize, discounts)));
        while let Some(Reverse((cost, city, disc))) = pq.pop() {
            if city == n - 1 {
                return cost;
            }
            if cost > dist[city][disc] {
                continue;
            }
            for &(v, w) in &g[city] {
                if cost + w < dist[v][disc] {
                    dist[v][disc] = cost + w;
                    pq.push(Reverse((dist[v][disc], v, disc)));
                }
                if disc > 0 && cost + w / 2 < dist[v][disc - 1] {
                    dist[v][disc - 1] = cost + w / 2;
                    pq.push(Reverse((dist[v][disc - 1], v, disc - 1)));
                }
            }
        }
        -1
    }
}
