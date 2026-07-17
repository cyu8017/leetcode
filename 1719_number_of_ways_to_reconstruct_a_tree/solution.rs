// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn check_ways(pairs: Vec<Vec<i32>>) -> i32 {
        let mut graph: HashMap<i32, HashSet<i32>> = HashMap::new();
        for pair in &pairs {
            let (a, b) = (pair[0], pair[1]);
            graph.entry(a).or_default().insert(b);
            graph.entry(b).or_default().insert(a);
        }
        let n = graph.len();
        let root = graph
            .iter()
            .find(|(_, neighbors)| neighbors.len() == n - 1)
            .map(|(&node, _)| node);
        let root = match root {
            Some(root) => root,
            None => return 0,
        };
        let mut ans = 1;
        for (&node, neighbors) in &graph {
            if node == root {
                continue;
            }
            let mut parent = None;
            let mut parent_degree = n + 1;
            for &nei in neighbors {
                let nei_degree = graph[&nei].len();
                if nei_degree >= neighbors.len() && nei_degree < parent_degree {
                    parent = Some(nei);
                    parent_degree = nei_degree;
                }
            }
            let parent = match parent {
                Some(parent) => parent,
                None => return 0,
            };
            for &nei in neighbors {
                if nei != parent && !graph[&parent].contains(&nei) {
                    return 0;
                }
            }
            if graph[&parent].len() == neighbors.len() {
                ans = 2;
            }
        }
        ans
    }
}
