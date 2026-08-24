// LeetCode 0886 - Possible Bipartition
// https://leetcode.com/problems/possible-bipartition/

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn possible_bipartition(n: i32, dislikes: Vec<Vec<i32>>) -> bool {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n + 1];
        for e in &dislikes {
            graph[e[0] as usize].push(e[1]);
            graph[e[1] as usize].push(e[0]);
        }
        let mut color = HashMap::new();
        for start in 1..=n as i32 {
            if color.contains_key(&start) {
                continue;
            }
            let mut queue = VecDeque::new();
            queue.push_back(start);
            color.insert(start, 0);
            while let Some(node) = queue.pop_front() {
                for &nei in &graph[node as usize] {
                    if !color.contains_key(&nei) {
                        color.insert(nei, color[&node] ^ 1);
                        queue.push_back(nei);
                    } else if color[&nei] == color[&node] {
                        return false;
                    }
                }
            }
        }
        true
    }
}
