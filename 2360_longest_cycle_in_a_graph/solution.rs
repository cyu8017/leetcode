// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

use std::collections::HashMap;

impl Solution {
    pub fn longest_cycle(edges: Vec<i32>) -> i32 {
        let n = edges.len();
        let mut vis = vec![false; n];
        let mut ans = -1;
        for i in 0..n {
            if vis[i] {
                continue;
            }
            let mut dist = HashMap::new();
            let mut cur = i as i32;
            let mut step = 0;
            while cur != -1 && !vis[cur as usize] {
                vis[cur as usize] = true;
                dist.insert(cur, step);
                cur = edges[cur as usize];
                step += 1;
            }
            if cur != -1 {
                if let Some(&prev) = dist.get(&cur) {
                    ans = ans.max(step - prev);
                }
            }
        }
        ans
    }
}
