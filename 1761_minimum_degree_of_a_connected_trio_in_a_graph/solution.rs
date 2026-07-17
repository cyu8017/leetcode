// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

impl Solution {
    pub fn min_trio_degree(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj = vec![vec![false; n]; n];
        let mut degree = vec![0i32; n];
        for e in &edges {
            let u = (e[0] - 1) as usize;
            let v = (e[1] - 1) as usize;
            adj[u][v] = true;
            adj[v][u] = true;
            degree[u] += 1;
            degree[v] += 1;
        }
        let mut best = i32::MAX;
        for e in &edges {
            let u = (e[0] - 1) as usize;
            let v = (e[1] - 1) as usize;
            for k in 0..n {
                if adj[u][k] && adj[v][k] {
                    best = best.min(degree[u] + degree[v] + degree[k] - 6);
                }
            }
        }
        if best == i32::MAX { -1 } else { best }
    }
}
