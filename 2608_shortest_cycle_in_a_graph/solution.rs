// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

use std::collections::VecDeque;

impl Solution {
    pub fn find_shortest_cycle(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        const INF: i32 = 1_000_000_000;
        let mut ans = INF;
        for start in 0..n {
            let mut dist = vec![-1; n];
            let mut parent = vec![-1i32; n];
            let mut q = VecDeque::new();
            q.push_back(start);
            dist[start] = 0;
            while let Some(u) = q.pop_front() {
                for &v in &g[u] {
                    if dist[v] < 0 {
                        dist[v] = dist[u] + 1;
                        parent[v] = u as i32;
                        q.push_back(v);
                    } else if parent[u] != v as i32 {
                        let c = dist[u] + dist[v] + 1;
                        if c < ans {
                            ans = c;
                        }
                    }
                }
            }
        }
        if ans == INF {
            -1
        } else {
            ans
        }
    }
}
