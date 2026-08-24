// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

use std::collections::VecDeque;

impl Solution {
    pub fn magnificent_sets(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        let mut color = vec![-1i32; n + 1];
        let mut components = Vec::new();
        for i in 1..=n {
            if color[i] != -1 {
                continue;
            }
            let mut comp = Vec::new();
            let mut q = VecDeque::new();
            q.push_back(i);
            color[i] = 0;
            let mut bipartite = true;
            while let Some(u) = q.pop_front() {
                comp.push(u);
                for &v in &g[u] {
                    if color[v] == -1 {
                        color[v] = color[u] ^ 1;
                        q.push_back(v);
                    } else if color[v] == color[u] {
                        bipartite = false;
                    }
                }
            }
            if !bipartite {
                return -1;
            }
            components.push(comp);
        }
        fn bfs_depth(start: usize, n: usize, g: &[Vec<usize>]) -> i32 {
            let mut dist = vec![-1; n + 1];
            let mut q = VecDeque::new();
            q.push_back(start);
            dist[start] = 1;
            let mut best = 1;
            while let Some(u) = q.pop_front() {
                if dist[u] > best {
                    best = dist[u];
                }
                for &v in &g[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            best
        }
        let mut ans = 0;
        for comp in &components {
            let mut best = 0;
            for &u in comp {
                let d = bfs_depth(u, n, &g);
                if d > best {
                    best = d;
                }
            }
            ans += best;
        }
        ans
    }
}
