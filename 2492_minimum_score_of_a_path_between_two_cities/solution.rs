// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

use std::collections::VecDeque;

impl Solution {
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for r in &roads {
            let (a, b, w) = (r[0] as usize, r[1] as usize, r[2]);
            g[a].push((b, w));
            g[b].push((a, w));
        }
        let mut vis = vec![false; n + 1];
        let mut ans = 1 << 30;
        let mut q = VecDeque::new();
        q.push_back(1);
        vis[1] = true;
        while let Some(u) = q.pop_front() {
            for &(v, w) in &g[u] {
                if w < ans {
                    ans = w;
                }
                if !vis[v] {
                    vis[v] = true;
                    q.push_back(v);
                }
            }
        }
        ans
    }
}
