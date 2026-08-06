// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(PartialEq)]
struct ProbItem {
    prob: f64,
    node: usize,
}

impl Eq for ProbItem {}

impl PartialOrd for ProbItem {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        self.prob.partial_cmp(&other.prob)
    }
}

impl Ord for ProbItem {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap_or(Ordering::Equal)
    }
}

impl Solution {
    pub fn max_probability(
        n: i32,
        edges: Vec<Vec<i32>>,
        succ_prob: Vec<f64>,
        start_node: i32,
        end_node: i32,
    ) -> f64 {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for (i, e) in edges.iter().enumerate() {
            let a = e[0] as usize;
            let b = e[1] as usize;
            let p = succ_prob[i];
            graph[a].push((b, p));
            graph[b].push((a, p));
        }
        let mut best = vec![0.0; n];
        best[start_node as usize] = 1.0;
        let mut heap = BinaryHeap::new();
        heap.push(ProbItem {
            prob: 1.0,
            node: start_node as usize,
        });
        while let Some(item) = heap.pop() {
            if item.node == end_node as usize {
                return item.prob;
            }
            if item.prob < best[item.node] {
                continue;
            }
            for &(to, edge_prob) in &graph[item.node] {
                let candidate = item.prob * edge_prob;
                if candidate > best[to] {
                    best[to] = candidate;
                    heap.push(ProbItem {
                        prob: candidate,
                        node: to,
                    });
                }
            }
        }
        0.0
    }
}
