// LeetCode 3558 - Number of Ways to Assign Edge Weights I
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

impl Solution {
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = edges.len() + 1;
        let mut g = vec![Vec::<usize>::new(); n + 1];
        for e in &edges {
            let (u, v) = (e[0] as usize, e[1] as usize);
            g[u].push(v);
            g[v].push(u);
        }
        fn dfs(i: usize, fa: usize, g: &[Vec<usize>]) -> i32 {
            let mut res = 0;
            for &j in &g[i] {
                if j != fa {
                    res = res.max(dfs(j, i, g) + 1);
                }
            }
            res
        }
        fn pow2(mut exp: i32) -> i32 {
            let mut a = 2i64;
            let mut res = 1i64;
            while exp > 0 {
                if exp & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                exp >>= 1;
            }
            res as i32
        }
        pow2(dfs(1, 0, &g) - 1)
    }
}
