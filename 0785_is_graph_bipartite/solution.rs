// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let n = graph.len();
        let mut color = vec![-1; n];
        for node in 0..n {
            if color[node] == -1 && !Self::dfs(&graph, node, 0, &mut color) {
                return false;
            }
        }
        true
    }

    fn dfs(graph: &[Vec<i32>], node: usize, c: i32, color: &mut [i32]) -> bool {
        color[node] = c;
        for &nei in &graph[node] {
            let nei = nei as usize;
            if color[nei] == -1 {
                if !Self::dfs(graph, nei, c ^ 1, color) {
                    return false;
                }
            } else if color[nei] == c {
                return false;
            }
        }
        true
    }
}
