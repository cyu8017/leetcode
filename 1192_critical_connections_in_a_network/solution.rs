// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

impl Solution {
    pub fn critical_connections(n: i32, connections: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in connections {
            graph[e[0] as usize].push(e[1] as usize);
            graph[e[1] as usize].push(e[0] as usize);
        }
        let mut disc = vec![-1i32; n];
        let mut low = vec![0i32; n];
        let mut time = 0i32;
        let mut bridges = Vec::new();
        fn dfs(
            node: usize,
            parent: i32,
            graph: &[Vec<usize>],
            disc: &mut [i32],
            low: &mut [i32],
            time: &mut i32,
            bridges: &mut Vec<Vec<i32>>,
        ) {
            disc[node] = *time;
            low[node] = *time;
            *time += 1;
            for &nxt in &graph[node] {
                if nxt as i32 == parent {
                    continue;
                }
                if disc[nxt] == -1 {
                    dfs(nxt, node as i32, graph, disc, low, time, bridges);
                    low[node] = low[node].min(low[nxt]);
                    if low[nxt] > disc[node] {
                        let (a, b) = if node < nxt {
                            (node as i32, nxt as i32)
                        } else {
                            (nxt as i32, node as i32)
                        };
                        bridges.push(vec![a, b]);
                    }
                } else {
                    low[node] = low[node].min(disc[nxt]);
                }
            }
        }
        dfs(0, -1, &graph, &mut disc, &mut low, &mut time, &mut bridges);
        bridges
    }
}
