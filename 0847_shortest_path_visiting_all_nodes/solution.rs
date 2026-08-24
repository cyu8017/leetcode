// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn shortest_path_length(graph: Vec<Vec<i32>>) -> i32 {
        let n = graph.len();
        let target = (1 << n) - 1;
        let mut queue = VecDeque::new();
        let mut seen = HashSet::new();
        for i in 0..n {
            queue.push_back((i, 1 << i, 0));
            seen.insert(((i as i64) << 20) | (1 << i));
        }
        while let Some((node, mask, dist)) = queue.pop_front() {
            if mask == target {
                return dist;
            }
            for &nxt in &graph[node] {
                let nxt = nxt as usize;
                let nmask = mask | (1 << nxt);
                let state = ((nxt as i64) << 20) | nmask as i64;
                if seen.insert(state) {
                    queue.push_back((nxt, nmask, dist + 1));
                }
            }
        }
        -1
    }
}
