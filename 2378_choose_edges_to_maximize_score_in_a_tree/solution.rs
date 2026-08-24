// LeetCode 2378 - Choose Edges to Maximize Score in a Tree
// https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

impl Solution {
    pub fn max_score(edges: Vec<Vec<i32>>) -> i64 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for i in 1..n {
            let p = edges[i - 1][0] as usize;
            let w = edges[i - 1][1];
            g[p].push((i, w));
            g[i].push((p, w));
        }
        fn dfs(u: usize, p: i32, g: &[Vec<(usize, i32)>]) -> (i64, i64) {
            let mut base = 0i64;
            let mut best_gain = 0i64;
            for &(to, w) in &g[u] {
                if to as i32 == p {
                    continue;
                }
                let (without, with) = dfs(to, u as i32, g);
                base += without;
                let gain = with + w as i64 - without;
                if gain > best_gain {
                    best_gain = gain;
                }
            }
            (base + best_gain, base)
        }
        dfs(0, -1, &g).0
    }
}
