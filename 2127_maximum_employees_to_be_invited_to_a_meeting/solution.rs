// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_invitations(favorite: Vec<i32>) -> i32 {
        let n = favorite.len();
        let mut indeg = vec![0; n];
        let mut depth = vec![1; n];
        for &f in &favorite {
            indeg[f as usize] += 1;
        }
        let mut q = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }
        while let Some(u) = q.pop_front() {
            let v = favorite[u] as usize;
            depth[v] = depth[v].max(depth[u] + 1);
            indeg[v] -= 1;
            if indeg[v] == 0 {
                q.push_back(v);
            }
        }
        let mut pair_sum = 0;
        let mut max_cycle = 0;
        let mut vis = vec![false; n];
        for i in 0..n {
            if indeg[i] == 0 || vis[i] {
                continue;
            }
            let mut u = i;
            let mut len_cycle = 0;
            while !vis[u] {
                vis[u] = true;
                u = favorite[u] as usize;
                len_cycle += 1;
            }
            if len_cycle == 2 {
                pair_sum += depth[i] + depth[favorite[i] as usize];
            } else {
                max_cycle = max_cycle.max(len_cycle);
            }
        }
        pair_sum.max(max_cycle)
    }
}
