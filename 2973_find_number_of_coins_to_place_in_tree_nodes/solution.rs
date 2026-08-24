// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

impl Solution {
    pub fn placed_coins(edges: Vec<Vec<i32>>, cost: Vec<i32>) -> Vec<i64> {
        let n = cost.len();
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = vec![0i64; n];
        fn dfs(u: usize, p: i32, g: &[Vec<usize>], cost: &[i32], ans: &mut [i64]) -> Vec<i32> {
            let mut vals = vec![cost[u]];
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let mut child = dfs(v, u as i32, g, cost, ans);
                vals.append(&mut child);
            }
            vals.sort_unstable();
            if vals.len() < 3 {
                ans[u] = 1;
            } else {
                let m = vals.len();
                let cand1 = vals[m - 1] as i64 * vals[m - 2] as i64 * vals[m - 3] as i64;
                let cand2 = vals[0] as i64 * vals[1] as i64 * vals[m - 1] as i64;
                let mut best = cand1.max(cand2);
                if best < 0 {
                    best = 0;
                }
                ans[u] = best;
            }
            if vals.len() <= 5 {
                return vals;
            }
            vec![
                vals[0],
                vals[1],
                vals[vals.len() - 3],
                vals[vals.len() - 2],
                vals[vals.len() - 1],
            ]
        }
        dfs(0, -1, &g, &cost, &mut ans);
        ans
    }
}
