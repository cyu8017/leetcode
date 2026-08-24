// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

impl Solution {
    pub fn min_cost(n: i32, mut edges: Vec<Vec<i32>>, k: i32) -> i32 {
        edges.sort_by_key(|e| e[2]);
        let n = n as usize;
        let check = |idx: usize| -> bool {
            let mut g = vec![Vec::new(); n];
            for i in 0..=idx {
                g[edges[i][0] as usize].push(edges[i][1] as usize);
                g[edges[i][1] as usize].push(edges[i][0] as usize);
            }
            let mut q = vec![0usize];
            let mut vis = vec![false; n];
            vis[0] = true;
            let mut dist = 0;
            while !q.is_empty() {
                let mut nq = Vec::new();
                for &u in &q {
                    if u == n - 1 {
                        return dist <= k;
                    }
                    for &v in &g[u] {
                        if !vis[v] {
                            vis[v] = true;
                            nq.push(v);
                        }
                    }
                }
                q = nq;
                dist += 1;
            }
            false
        };
        let m = edges.len();
        if m == 0 {
            return -1;
        }
        let mut l = 0usize;
        let mut r = m - 1;
        while l < r {
            let mid = (l + r) >> 1;
            if check(mid) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if check(l) {
            edges[l][2]
        } else {
            -1
        }
    }
}
