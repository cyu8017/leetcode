// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

use std::collections::{BTreeSet, VecDeque};

impl Solution {
    pub fn get_ancestors(n: i32, edges: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        let mut indeg = vec![0; n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            indeg[e[1] as usize] += 1;
        }
        let mut anc = vec![BTreeSet::new(); n];
        let mut q = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                q.push_back(i);
            }
        }
        while let Some(u) = q.pop_front() {
            let u_anc: Vec<i32> = anc[u].iter().copied().collect();
            for &v in &g[u] {
                anc[v].insert(u as i32);
                for a in &u_anc {
                    anc[v].insert(*a);
                }
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    q.push_back(v);
                }
            }
        }
        anc.into_iter().map(|s| s.into_iter().collect()).collect()
    }
}
