// LeetCode 3367 - Maximize Sum of Weights after Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

impl Solution {
    pub fn maximize_sum_of_weights(edges: Vec<Vec<i32>>, k: i32) -> i64 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        fn dfs(u: usize, p: i32, g: &[Vec<(usize, i32)>], k: i32) -> (i64, i64) {
            let mut base = 0i64;
            let mut gains = Vec::new();
            for &(to, w) in &g[u] {
                if to as i32 == p {
                    continue;
                }
                let (keep, drop) = dfs(to, u as i32, g, k);
                base += drop;
                let gain = keep + w as i64 - drop;
                if gain > 0 {
                    gains.push(gain);
                }
            }
            gains.sort_unstable_by(|a, b| b.cmp(a));
            let mut with = base;
            let mut without = base;
            for i in 0..gains.len() {
                if i < (k - 1) as usize {
                    with += gains[i];
                }
                if i < k as usize {
                    without += gains[i];
                }
            }
            (with, without)
        }
        dfs(0, -1, &g, k).1
    }
}
