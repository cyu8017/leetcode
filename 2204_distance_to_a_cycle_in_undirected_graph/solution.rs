// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

use std::collections::VecDeque;

impl Solution {
    pub fn distance_to_cycle(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        let mut deg = vec![0; n];
        for e in edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
            deg[a] += 1;
            deg[b] += 1;
        }
        let mut q = VecDeque::new();
        for i in 0..n {
            if deg[i] == 1 {
                q.push_back(i);
            }
        }
        let mut on_cycle = vec![true; n];
        while let Some(u) = q.pop_front() {
            on_cycle[u] = false;
            for &v in &g[u] {
                deg[v] -= 1;
                if deg[v] == 1 {
                    q.push_back(v);
                }
            }
        }
        let mut ans = vec![-1; n];
        let mut qq = VecDeque::new();
        for i in 0..n {
            if on_cycle[i] {
                ans[i] = 0;
                qq.push_back(i);
            }
        }
        while let Some(u) = qq.pop_front() {
            for &v in &g[u] {
                if ans[v] == -1 {
                    ans[v] = ans[u] + 1;
                    qq.push_back(v);
                }
            }
        }
        ans
    }
}
