// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

use std::collections::VecDeque;

impl Solution {
    pub fn shortest_alternating_paths(
        n: i32,
        red_edges: Vec<Vec<i32>>,
        blue_edges: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        let n = n as usize;
        let mut graph = [vec![Vec::new(); n], vec![Vec::new(); n]];
        for e in red_edges {
            graph[0][e[0] as usize].push(e[1] as usize);
        }
        for e in blue_edges {
            graph[1][e[0] as usize].push(e[1] as usize);
        }
        let mut ans = vec![-1; n];
        let mut queue = VecDeque::new();
        queue.push_back((0usize, 0usize, 0i32));
        queue.push_back((0, 1, 0));
        let mut seen = [vec![false; n], vec![false; n]];
        seen[0][0] = true;
        seen[1][0] = true;
        while let Some((node, color, dist)) = queue.pop_front() {
            if ans[node] == -1 {
                ans[node] = dist;
            }
            let next_color = 1 - color;
            for &nxt in &graph[color][node] {
                if !seen[next_color][nxt] {
                    seen[next_color][nxt] = true;
                    queue.push_back((nxt, next_color, dist + 1));
                }
            }
        }
        ans
    }
}
