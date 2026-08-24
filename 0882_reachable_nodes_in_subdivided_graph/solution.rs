// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn reachable_nodes(edges: Vec<Vec<i32>>, max_moves: i32, n: i32) -> i32 {
        let n = n as usize;
        let mut graph = vec![HashMap::new(); n];
        for e in &edges {
            graph[e[0] as usize].insert(e[1], e[2]);
            graph[e[1] as usize].insert(e[0], e[2]);
        }
        let mut pq = BinaryHeap::new();
        pq.push((max_moves, 0));
        let mut seen = HashMap::new();
        while let Some((moves, node)) = pq.pop() {
            if seen.contains_key(&node) {
                continue;
            }
            seen.insert(node, moves);
            for (&nei, &cnt) in &graph[node as usize] {
                let remain = moves - cnt - 1;
                if !seen.contains_key(&nei) && remain >= 0 {
                    pq.push((remain, nei));
                }
            }
        }
        let mut ans = seen.len() as i32;
        for e in &edges {
            let left = *seen.get(&e[0]).unwrap_or(&0);
            let right = *seen.get(&e[1]).unwrap_or(&0);
            ans += e[2].min(left + right);
        }
        ans
    }
}
