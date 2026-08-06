// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn tree_diameter(edges: Vec<Vec<i32>>) -> i32 {
        if edges.is_empty() {
            return 0;
        }
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for e in &edges {
            graph.entry(e[0]).or_default().push(e[1]);
            graph.entry(e[1]).or_default().push(e[0]);
        }
        let farthest = |start: i32| -> (i32, i32) {
            let mut q = VecDeque::new();
            q.push_back((start, 0));
            let mut seen = HashSet::new();
            seen.insert(start);
            let mut last = (start, 0);
            while let Some((node, dist)) = q.pop_front() {
                last = (node, dist);
                if let Some(neis) = graph.get(&node) {
                    for &v in neis {
                        if seen.insert(v) {
                            q.push_back((v, dist + 1));
                        }
                    }
                }
            }
            last
        };
        let (endpoint, _) = farthest(edges[0][0]);
        farthest(endpoint).1
    }
}
