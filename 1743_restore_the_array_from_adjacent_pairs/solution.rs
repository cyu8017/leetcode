// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for pair in &adjacent_pairs {
            graph.entry(pair[0]).or_default().push(pair[1]);
            graph.entry(pair[1]).or_default().push(pair[0]);
        }
        let start = *graph
            .iter()
            .find(|(_, neighbors)| neighbors.len() == 1)
            .map(|(node, _)| node)
            .unwrap();
        let n = graph.len();
        let mut ans = Vec::with_capacity(n);
        ans.push(start);
        let mut prev: Option<i32> = None;
        while ans.len() < n {
            let cur = *ans.last().unwrap();
            let neighbors = &graph[&cur];
            let nxt = if prev != Some(neighbors[0]) {
                neighbors[0]
            } else {
                neighbors[1]
            };
            ans.push(nxt);
            prev = Some(cur);
        }
        ans
    }
}
