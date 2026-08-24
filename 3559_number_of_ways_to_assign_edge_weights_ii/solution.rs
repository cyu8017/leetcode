// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

impl Solution {
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        const LOG: usize = 17;
        let n = edges.len() + 1;
        let mut depth = vec![0i32; n + 1];
        let mut graph = vec![Vec::<usize>::new(); n + 1];
        let mut parent = vec![vec![-1i32; n + 1]; LOG];
        for e in &edges {
            let (u, v) = (e[0] as usize, e[1] as usize);
            graph[u].push(v);
            graph[v].push(u);
        }
        fn dfs(u: usize, p: i32, graph: &[Vec<usize>], parent: &mut [Vec<i32>], depth: &mut [i32]) {
            parent[0][u] = p;
            for &v in &graph[u] {
                if v as i32 != p {
                    depth[v] = depth[u] + 1;
                    dfs(v, u as i32, graph, parent, depth);
                }
            }
        }
        dfs(1, -1, &graph, &mut parent, &mut depth);
        for k in 1..LOG {
            for v in 1..=n {
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
        let mod_pow = |mut exp: i32| -> i32 {
            let mut base = 2i64;
            let mut res = 1i64;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = res * base % MOD;
                }
                base = base * base % MOD;
                exp >>= 1;
            }
            res as i32
        };
        queries
            .iter()
            .map(|q| {
                let (u, v) = (q[0] as usize, q[1] as usize);
                if u == v {
                    return 0;
                }
                let a = lca(u, v, &parent, &depth);
                let d = depth[u] + depth[v] - 2 * depth[a];
                mod_pow(d - 1)
            })
            .collect()
    }
}
