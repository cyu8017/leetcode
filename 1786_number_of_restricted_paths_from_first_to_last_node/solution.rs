// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn count_restricted_paths(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n + 1];
        for e in &edges {
            let (a, b, w) = (e[0] as usize, e[1] as usize, e[2] as i64);
            adj[a].push((b, w));
            adj[b].push((a, w));
        }
        let mut dist = vec![i64::MAX; n + 1];
        dist[n] = 0;
        let mut heap = BinaryHeap::new();
        heap.push(Reverse((0i64, n)));
        while let Some(Reverse((d, u))) = heap.pop() {
            if d != dist[u] {
                continue;
            }
            for &(v, w) in &adj[u] {
                let nd = d + w;
                if nd < dist[v] {
                    dist[v] = nd;
                    heap.push(Reverse((nd, v)));
                }
            }
        }
        let mut order: Vec<usize> = (1..=n).collect();
        order.sort_by_key(|&u| dist[u]);
        const MOD: i64 = 1_000_000_007;
        let mut cnt = vec![0i64; n + 1];
        cnt[n] = 1;
        for &u in &order {
            if u == n {
                continue;
            }
            for &(v, _) in &adj[u] {
                if dist[u] > dist[v] {
                    cnt[u] = (cnt[u] + cnt[v]) % MOD;
                }
            }
        }
        cnt[1] as i32
    }
}
