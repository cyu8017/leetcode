// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

impl Solution {
    pub fn closest_node(n: i32, edges: Vec<Vec<i32>>, query: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        const LOG: usize = 17;
        let mut up = vec![vec![0usize; n]; LOG];
        let mut depth = vec![0i32; n];
        fn dfs(u: usize, p: usize, g: &[Vec<usize>], up: &mut [Vec<usize>], depth: &mut [i32]) {
            up[0][u] = p;
            for &v in &g[u] {
                if v != p {
                    depth[v] = depth[u] + 1;
                    dfs(v, u, g, up, depth);
                }
            }
        }
        dfs(0, 0, &g, &mut up, &mut depth);
        for k in 1..LOG {
            for v in 0..n {
                up[k][v] = up[k - 1][up[k - 1][v]];
            }
        }
        let lift = |mut v: usize, d: i32, up: &[Vec<usize>]| {
            for k in 0..LOG {
                if (d >> k) & 1 == 1 {
                    v = up[k][v];
                }
            }
            v
        };
        let lca = |mut a: usize, mut b: usize, up: &[Vec<usize>], depth: &[i32]| {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            a = lift(a, depth[a] - depth[b], up);
            if a == b {
                return a;
            }
            for k in (0..LOG).rev() {
                if up[k][a] != up[k][b] {
                    a = up[k][a];
                    b = up[k][b];
                }
            }
            up[0][a]
        };
        let dist = |a: usize, b: usize, up: &[Vec<usize>], depth: &[i32]| {
            let c = lca(a, b, up, depth);
            depth[a] + depth[b] - 2 * depth[c]
        };
        let mut ans = vec![0; query.len()];
        for (i, q) in query.iter().enumerate() {
            let a = q[0] as usize;
            let b = q[1] as usize;
            let x = q[2] as usize;
            let cands = [lca(a, b, &up, &depth), lca(a, x, &up, &depth), lca(b, x, &up, &depth)];
            let mut best = cands[0];
            let mut best_d = dist(cands[0], x, &up, &depth);
            for &t in &cands[1..] {
                let d = dist(t, x, &up, &depth);
                if d < best_d {
                    best_d = d;
                    best = t;
                }
            }
            ans[i] = best as i32;
        }
        ans
    }
}
