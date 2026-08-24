// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

impl Solution {
    pub fn min_operations_queries(n: i32, edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2] as usize));
            g[e[1] as usize].push((e[0] as usize, e[2] as usize));
        }
        const LOG: usize = 15;
        let mut up = vec![vec![0usize; n]; LOG];
        let mut depth = vec![0i32; n];
        let mut cnt = vec![[0i32; 27]; n];
        fn dfs(
            u: usize,
            p: usize,
            g: &[Vec<(usize, usize)>],
            up: &mut [Vec<usize>],
            depth: &mut [i32],
            cnt: &mut [[i32; 27]],
        ) {
            up[0][u] = p;
            for &(v, w) in &g[u] {
                if v == p {
                    continue;
                }
                depth[v] = depth[u] + 1;
                cnt[v] = cnt[u];
                cnt[v][w] += 1;
                dfs(v, u, g, up, depth, cnt);
            }
        }
        dfs(0, 0, &g, &mut up, &mut depth, &mut cnt);
        for j in 1..LOG {
            for i in 0..n {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }
        let lca = |mut a: usize, mut b: usize, up: &[Vec<usize>], depth: &[i32]| -> usize {
            if depth[a] < depth[b] {
                std::mem::swap(&mut a, &mut b);
            }
            let mut diff = depth[a] - depth[b];
            for j in 0..LOG {
                if (diff & (1 << j)) != 0 {
                    a = up[j][a];
                }
            }
            if a == b {
                return a;
            }
            for j in (0..LOG).rev() {
                if up[j][a] != up[j][b] {
                    a = up[j][a];
                    b = up[j][b];
                }
            }
            up[0][a]
        };
        queries
            .into_iter()
            .map(|q| {
                let a = q[0] as usize;
                let b = q[1] as usize;
                let c = lca(a, b, &up, &depth);
                let total = depth[a] + depth[b] - 2 * depth[c];
                let mut best = 0;
                for w in 1..=26 {
                    let f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
                    best = best.max(f);
                }
                total - best
            })
            .collect()
    }
}
