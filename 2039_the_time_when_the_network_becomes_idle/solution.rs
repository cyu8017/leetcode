// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

use std::collections::VecDeque;

impl Solution {
    pub fn network_becomes_idle(edges: Vec<Vec<i32>>, patience: Vec<i32>) -> i32 {
        let n = patience.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut dist = vec![-1; n];
        let mut q = VecDeque::new();
        q.push_back(0);
        dist[0] = 0;
        while let Some(u) = q.pop_front() {
            for &v in &g[u] {
                if dist[v] == -1 {
                    dist[v] = dist[u] + 1;
                    q.push_back(v);
                }
            }
        }
        let mut ans = 0;
        for i in 1..n {
            let round = dist[i] * 2;
            let last_send = (round - 1) / patience[i] * patience[i];
            ans = ans.max(last_send + round);
        }
        ans + 1
    }
}
