// LeetCode 3243 - Shortest Distance After Road Addition Queries I
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

use std::collections::VecDeque;

impl Solution {
    pub fn shortest_distance_after_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for i in 0..n - 1 {
            g[i].push(i + 1);
        }
        let bfs = |g: &[Vec<usize>]| -> i32 {
            let mut q = VecDeque::new();
            q.push_back(0);
            let mut vis = vec![false; n];
            vis[0] = true;
            let mut d = 0;
            loop {
                let k = q.len();
                for _ in 0..k {
                    let u = q.pop_front().unwrap();
                    if u == n - 1 {
                        return d;
                    }
                    for &v in &g[u] {
                        if !vis[v] {
                            vis[v] = true;
                            q.push_back(v);
                        }
                    }
                }
                d += 1;
            }
        };
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            g[q[0] as usize].push(q[1] as usize);
            ans[i] = bfs(&g);
        }
        ans
    }
}
