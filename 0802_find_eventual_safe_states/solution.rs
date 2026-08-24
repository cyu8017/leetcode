// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let n = graph.len();
        let mut color = vec![0i32; n];
        let mut ans = Vec::new();
        for i in 0..n {
            if Self::dfs(&graph, i, &mut color) {
                ans.push(i as i32);
            }
        }
        ans
    }

    fn dfs(graph: &[Vec<i32>], node: usize, color: &mut [i32]) -> bool {
        if color[node] != 0 {
            return color[node] == 2;
        }
        color[node] = 1;
        for &nei in &graph[node] {
            if !Self::dfs(graph, nei as usize, color) {
                return false;
            }
        }
        color[node] = 2;
        true
    }
}
