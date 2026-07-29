// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

impl Solution {
    pub fn leads_to_destination(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in &edges {
            graph[e[0] as usize].push(e[1] as usize);
        }
        // 0 unvisited, 1 in progress, 2 confirmed
        let mut state = vec![0u8; n];
        Self::dfs(source as usize, destination as usize, &graph, &mut state)
    }

    fn dfs(node: usize, destination: usize, graph: &[Vec<usize>], state: &mut [u8]) -> bool {
        if graph[node].is_empty() {
            return node == destination;
        }
        if state[node] == 1 {
            return false;
        }
        if state[node] == 2 {
            return true;
        }
        state[node] = 1;
        for &nxt in &graph[node] {
            if !Self::dfs(nxt, destination, graph, state) {
                return false;
            }
        }
        state[node] = 2;
        true
    }
}
