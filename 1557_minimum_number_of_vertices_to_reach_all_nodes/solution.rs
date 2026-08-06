// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

use std::collections::HashSet;

impl Solution {
    pub fn find_smallest_set_of_vertices(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let incoming: HashSet<i32> = edges.iter().map(|e| e[1]).collect();
        (0..n).filter(|v| !incoming.contains(v)).collect()
    }
}
