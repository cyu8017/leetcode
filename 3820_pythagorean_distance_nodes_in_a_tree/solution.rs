// LeetCode 3820 - Pythagorean Distance Nodes in a Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

use std::collections::VecDeque;

impl Solution {
    pub fn special_nodes(n: i32, edges: Vec<Vec<i32>>, x: i32, y: i32, z: i32) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            g[a].push(b);
            g[b].push(a);
        }
        let bfs = |start: i32| {
            let mut dist = vec![1_000_000_000; n];
            let mut q = VecDeque::new();
            dist[start as usize] = 0;
            q.push_back(start as usize);
            while let Some(u) = q.pop_front() {
                for &v in &g[u] {
                    if dist[v] > dist[u] + 1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            dist
        };
        let d1 = bfs(x);
        let d2 = bfs(y);
        let d3 = bfs(z);
        let mut ans = 0;
        for i in 0..n {
            let mut a = [d1[i], d2[i], d3[i]];
            a.sort_unstable();
            let x0 = a[0] as i64;
            let x1 = a[1] as i64;
            let x2 = a[2] as i64;
            if x0 * x0 + x1 * x1 == x2 * x2 {
                ans += 1;
            }
        }
        ans
    }
}
