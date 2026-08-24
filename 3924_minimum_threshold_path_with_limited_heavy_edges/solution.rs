// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

use std::collections::VecDeque;

impl Solution {
    pub fn min_threshold(n: i32, edges: Vec<Vec<i32>>, source: i32, target: i32, k: i32) -> i32 {
        if source == target {
            return 0;
        }
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        let mut max_weight = 0;
        for e in &edges {
            let (u, v, w) = (e[0] as usize, e[1] as usize, e[2]);
            g[u].push((v, w));
            g[v].push((u, w));
            max_weight = max_weight.max(w);
        }
        let can = |threshold: i32| -> bool {
            const INF: i32 = 1_000_000_000;
            let mut dist = vec![INF; n];
            dist[source as usize] = 0;
            let mut dq = VecDeque::new();
            dq.push_back(source as usize);
            while let Some(u) = dq.pop_front() {
                for &(to, weight) in &g[u] {
                    let cost = if weight > threshold { 1 } else { 0 };
                    if dist[u] + cost >= dist[to] || dist[u] + cost > k {
                        continue;
                    }
                    dist[to] = dist[u] + cost;
                    if cost == 0 {
                        dq.push_front(to);
                    } else {
                        dq.push_back(to);
                    }
                }
            }
            dist[target as usize] <= k
        };
        if !can(max_weight) {
            return -1;
        }
        let mut lo = 0;
        let mut hi = max_weight;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if can(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
