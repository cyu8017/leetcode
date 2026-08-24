// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_max_path_score(edges: Vec<Vec<i32>>, online: Vec<bool>, k: i64) -> i32 {
        let n = online.len();
        let mut g = vec![Vec::new(); n];
        let mut l = i32::MAX;
        let mut r = 0;
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            let w = e[2];
            if !online[u] || !online[v] {
                continue;
            }
            g[u].push((v, w));
            l = l.min(w);
            r = r.max(w);
        }
        if l == i32::MAX {
            return -1;
        }
        let check = |mid: i32| -> bool {
            const INF: i32 = i32::MAX / 2;
            let mut dist = vec![INF; n];
            dist[0] = 0;
            let mut pq: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
            pq.push(Reverse((0, 0)));
            while let Some(Reverse((d, u))) = pq.pop() {
                if d as i64 > k {
                    return false;
                }
                if u == n - 1 {
                    return true;
                }
                if dist[u] < d {
                    continue;
                }
                for &(v, w) in &g[u] {
                    if w < mid {
                        continue;
                    }
                    let nd = d + w;
                    if nd < dist[v] {
                        dist[v] = nd;
                        pq.push(Reverse((nd, v)));
                    }
                }
            }
            false
        };
        while l < r {
            let mid = (l + r + 1) >> 1;
            if check(mid) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        if check(l) {
            l
        } else {
            -1
        }
    }
}
