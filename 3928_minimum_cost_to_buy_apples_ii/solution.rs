// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct Edge {
    to: usize,
    empty: i32,
    full: i32,
}

impl Solution {
    pub fn min_cost_to_buy_apples(n: i32, prices: Vec<i32>, roads: Vec<Vec<i32>>) -> Vec<i64> {
        let n = n as usize;
        let mut g: Vec<Vec<Edge>> = (0..n).map(|_| Vec::new()).collect();
        for road in &roads {
            let e = Edge {
                to: road[1] as usize,
                empty: road[2],
                full: road[2] * road[3],
            };
            g[road[0] as usize].push(Edge {
                to: e.to,
                empty: e.empty,
                full: e.full,
            });
            g[road[1] as usize].push(Edge {
                to: road[0] as usize,
                empty: e.empty,
                full: e.full,
            });
        }
        const INF: i64 = 1 << 62;
        let dijkstra = |source: usize, carrying: bool| -> Vec<i64> {
            let mut dist = vec![INF; n];
            dist[source] = 0;
            let mut pq: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
            pq.push(Reverse((0, source)));
            while let Some(Reverse((d, node))) = pq.pop() {
                if d != dist[node] {
                    continue;
                }
                for e in &g[node] {
                    let weight = if carrying { e.full } else { e.empty };
                    let next = d + weight as i64;
                    if next < dist[e.to] {
                        dist[e.to] = next;
                        pq.push(Reverse((next, e.to)));
                    }
                }
            }
            dist
        };
        let mut answer = vec![0i64; n];
        for source in 0..n {
            let empty_dist = dijkstra(source, false);
            let full_dist = dijkstra(source, true);
            let mut best = prices[source] as i64;
            for shop in 0..n {
                if empty_dist[shop] == INF || full_dist[shop] == INF {
                    continue;
                }
                let total = empty_dist[shop] + full_dist[shop] + prices[shop] as i64;
                if total < best {
                    best = total;
                }
            }
            answer[source] = best;
        }
        answer
    }
}
