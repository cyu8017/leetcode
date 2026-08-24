// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

impl Solution {
    pub fn all_paths_source_target(graph: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let target = graph.len() as i32 - 1;
        let mut answer = Vec::new();
        let mut path = vec![0];
        Self::dfs(&graph, 0, target, &mut path, &mut answer);
        answer
    }

    fn dfs(
        graph: &[Vec<i32>],
        node: i32,
        target: i32,
        path: &mut Vec<i32>,
        answer: &mut Vec<Vec<i32>>,
    ) {
        if node == target {
            answer.push(path.clone());
            return;
        }
        for &nei in &graph[node as usize] {
            path.push(nei);
            Self::dfs(graph, nei, target, path, answer);
            path.pop();
        }
    }
}
