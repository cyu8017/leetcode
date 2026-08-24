// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

use std::collections::VecDeque;

impl Solution {
    pub fn last_marked_nodes(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let bfs = |start: usize| -> (usize, Vec<i32>) {
            let mut dist = vec![-1; n];
            let mut q = VecDeque::new();
            q.push_back(start);
            dist[start] = 0;
            let mut far = start;
            while let Some(u) = q.pop_front() {
                if dist[u] > dist[far] {
                    far = u;
                }
                for &v in &g[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            (far, dist)
        };
        let (u, _) = bfs(0);
        let (v, du) = bfs(u);
        let (_, dv) = bfs(v);
        (0..n).map(|i| if du[i] >= dv[i] { u as i32 } else { v as i32 }).collect()
    }
}
