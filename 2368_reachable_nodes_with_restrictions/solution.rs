// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn reachable_nodes(n: i32, edges: Vec<Vec<i32>>, restricted: Vec<i32>) -> i32 {
        let n = n as usize;
        let ban: HashSet<i32> = restricted.into_iter().collect();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut ans = 0;
        let mut vis = vec![false; n];
        let mut q = VecDeque::new();
        q.push_back(0);
        vis[0] = true;
        while let Some(u) = q.pop_front() {
            ans += 1;
            for &v in &g[u] {
                if !vis[v] && !ban.contains(&(v as i32)) {
                    vis[v] = true;
                    q.push_back(v);
                }
            }
        }
        ans
    }
}
