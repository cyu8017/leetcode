// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn count_subgraphs_for_each_diameter(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut adj = vec![vec![]; n];
        for e in edges {
            let (a, b) = (e[0] as usize - 1, e[1] as usize - 1);
            adj[a].push(b);
            adj[b].push(a);
        }
        let mut ans = vec![0; n - 1];
        let bfs = |mask: i32, src: usize| -> (usize, HashMap<usize, i32>) {
            let mut dist = HashMap::new();
            dist.insert(src, 0);
            let mut q = VecDeque::from([src]);
            while let Some(u) = q.pop_front() {
                for &v in &adj[u] {
                    if mask >> v & 1 == 1 && !dist.contains_key(&v) {
                        dist.insert(v, dist[&u] + 1);
                        q.push_back(v);
                    }
                }
            }
            let far = *dist.iter().max_by_key(|(_, d)| *d).map(|(k, _)| k).unwrap_or(&src);
            (far, dist)
        };
        for mask in 1..(1 << n) {
            if mask & (mask - 1) == 0 {
                continue;
            }
            let mut start = 0;
            while mask >> start & 1 == 0 {
                start += 1;
            }
            let (far, seen) = bfs(mask, start);
            if seen.len() == mask.count_ones() as usize {
                let (_, dist) = bfs(mask, far);
                let mx = *dist.values().max().unwrap_or(&0);
                ans[(mx - 1) as usize] += 1;
            }
        }
        ans
    }
}
