// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

use std::collections::HashSet;

impl Solution {
    pub fn is_possible(n: i32, edges: Vec<Vec<i32>>) -> bool {
        let n = n as usize;
        let mut deg = vec![0; n + 1];
        let mut adj = vec![HashSet::new(); n + 1];
        for e in &edges {
            let (u, v) = (e[0] as usize, e[1] as usize);
            deg[u] += 1;
            deg[v] += 1;
            adj[u].insert(v);
            adj[v].insert(u);
        }
        let mut odd = Vec::new();
        for i in 1..=n {
            if deg[i] % 2 == 1 {
                odd.push(i);
            }
        }
        if odd.is_empty() {
            return true;
        }
        if odd.len() == 2 {
            let (a, b) = (odd[0], odd[1]);
            if !adj[a].contains(&b) {
                return true;
            }
            for i in 1..=n {
                if i != a && i != b && !adj[a].contains(&i) && !adj[b].contains(&i) {
                    return true;
                }
            }
            return false;
        }
        if odd.len() == 4 {
            let (a, b, c, d) = (odd[0], odd[1], odd[2], odd[3]);
            return (!adj[a].contains(&b) && !adj[c].contains(&d))
                || (!adj[a].contains(&c) && !adj[b].contains(&d))
                || (!adj[a].contains(&d) && !adj[b].contains(&c));
        }
        false
    }
}
