// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

impl Solution {
    pub fn minimum_weight(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut g = vec![Vec::<(usize, i32)>::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        const LOG: usize = 17;
        let mut parent = vec![vec![-1i32; n]; LOG];
        let mut depth = vec![0i32; n];
        let mut dist = vec![0i32; n];
        fn dfs(u: usize, p: i32, g: &[Vec<(usize, i32)>], parent: &mut [Vec<i32>], depth: &mut [i32], dist: &mut [i32]) {
            parent[0][u] = p;
            for &(to, w) in &g[u] {
                if to as i32 == p {
                    continue;
                }
                depth[to] = depth[u] + 1;
                dist[to] = dist[u] + w;
                dfs(to, u as i32, g, parent, depth, dist);
            }
        }
        dfs(0, -1, &g, &mut parent, &mut depth, &mut dist);
        for k in 1..LOG {
            for v in 0..n {
                if parent[k - 1][v] != -1 {
                    parent[k][v] = parent[k - 1][parent[k - 1][v] as usize];
                }
            }
        }
        let lca = |mut u: usize, mut v: usize, parent: &[Vec<i32>], depth: &[i32]| -> usize {
            if depth[u] < depth[v] {
                std::mem::swap(&mut u, &mut v);
            }
            for k in (0..LOG).rev() {
                if parent[k][u] != -1 && depth[parent[k][u] as usize] >= depth[v] {
                    u = parent[k][u] as usize;
                }
            }
            if u == v {
                return u;
            }
            for k in (0..LOG).rev() {
                if parent[k][u] != -1 && parent[k][u] != parent[k][v] {
                    u = parent[k][u] as usize;
                    v = parent[k][v] as usize;
                }
            }
            parent[0][u] as usize
        };
        let path = |u: usize, v: usize, parent: &[Vec<i32>], depth: &[i32], dist: &[i32]| -> i32 {
            let a = lca(u, v, parent, depth);
            dist[u] + dist[v] - 2 * dist[a]
        };
        queries
            .iter()
            .map(|q| {
                let (a, b, c) = (q[0] as usize, q[1] as usize, q[2] as usize);
                (path(a, b, &parent, &depth, &dist) + path(b, c, &parent, &depth, &dist) + path(a, c, &parent, &depth, &dist)) / 2
            })
            .collect()
    }
}
