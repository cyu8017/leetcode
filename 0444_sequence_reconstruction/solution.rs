// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn sequence_reconstruction(nums: Vec<i32>, sequences: Vec<Vec<i32>>) -> bool {
        let mut indegree: HashMap<i32, i32> = HashMap::new();
        let mut graph: HashMap<i32, HashSet<i32>> = HashMap::new();
        let mut seen_edges: HashSet<(i32, i32)> = HashSet::new();

        for value in &nums {
            indegree.insert(*value, 0);
            graph.insert(*value, HashSet::new());
        }

        for sequence in sequences {
            for pair in sequence.windows(2) {
                let left = pair[0];
                let right = pair[1];
                if !seen_edges.insert((left, right)) {
                    continue;
                }
                if graph.get_mut(&left).unwrap().insert(right) {
                    *indegree.get_mut(&right).unwrap() += 1;
                }
            }
        }

        let mut queue = VecDeque::new();
        for value in &nums {
            if indegree[value] == 0 {
                queue.push_back(*value);
            }
        }

        let mut order = Vec::new();
        while let Some(node) = queue.pop_front() {
            if queue.len() > 0 {
                return false;
            }
            order.push(node);
            for neighbor in graph.get(&node).unwrap().iter().copied().collect::<Vec<_>>() {
                let entry = indegree.get_mut(&neighbor).unwrap();
                *entry -= 1;
                if *entry == 0 {
                    queue.push_back(neighbor);
                }
            }
        }

        order == nums
    }
}
