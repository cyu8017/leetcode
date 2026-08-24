// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

use std::collections::VecDeque;

impl Solution {
    pub fn min_max_weight(n: i32, edges: Vec<Vec<i32>>, _threshold: i32) -> i32 {
        let n = n as usize;
        let ok = |mid: i32| -> bool {
            let mut g = vec![Vec::new(); n];
            for e in &edges {
                let (a, b, w) = (e[0] as usize, e[1] as usize, e[2]);
                if w <= mid {
                    g[b].push(a);
                }
            }
            let mut vis = vec![false; n];
            let mut q = VecDeque::new();
            q.push_back(0);
            vis[0] = true;
            let mut cnt = 1;
            while let Some(u) = q.pop_front() {
                for &v in &g[u] {
                    if !vis[v] {
                        vis[v] = true;
                        cnt += 1;
                        q.push_back(v);
                    }
                }
            }
            cnt == n
        };
        let mut lo = 1;
        let mut hi = 1_000_001;
        let mut ans = -1;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                ans = mid;
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        ans
    }
}
