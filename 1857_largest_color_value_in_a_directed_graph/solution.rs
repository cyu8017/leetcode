// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

use std::collections::VecDeque;

impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {
        let n = colors.len();
        let bytes = colors.as_bytes();
        let mut indegree = vec![0i32; n];
        let mut adjacency = vec![Vec::new(); n];
        for edge in &edges {
            let from = edge[0] as usize;
            let to = edge[1] as usize;
            adjacency[from].push(to);
            indegree[to] += 1;
        }

        let mut queue: VecDeque<usize> = (0..n).filter(|&i| indegree[i] == 0).collect();
        let mut dp = vec![[0i32; 26]; n];
        for node in 0..n {
            dp[node][(bytes[node] - b'a') as usize] = 1;
        }

        let mut processed = 0;
        let mut answer = 0;
        while let Some(node) = queue.pop_front() {
            processed += 1;
            answer = answer.max(*dp[node].iter().max().unwrap_or(&0));
            let neighbor_color_base = bytes;
            for &neighbor in &adjacency[node] {
                let neighbor_color = (neighbor_color_base[neighbor] - b'a') as usize;
                for color_index in 0..26 {
                    let mut candidate = dp[node][color_index];
                    if color_index == neighbor_color {
                        candidate += 1;
                    }
                    if candidate > dp[neighbor][color_index] {
                        dp[neighbor][color_index] = candidate;
                    }
                }
                indegree[neighbor] -= 1;
                if indegree[neighbor] == 0 {
                    queue.push_back(neighbor);
                }
            }
        }
        if processed == n {
            answer
        } else {
            -1
        }
    }
}
