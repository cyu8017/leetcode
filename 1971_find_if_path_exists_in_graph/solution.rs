// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        if source == destination {
            return true;
        }
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            g[a].push(b);
            g[b].push(a);
        }
        let mut stack = vec![source as usize];
        let mut seen = vec![false; n];
        seen[source as usize] = true;
        while let Some(u) = stack.pop() {
            if u == destination as usize {
                return true;
            }
            for &v in &g[u] {
                if !seen[v] {
                    seen[v] = true;
                    stack.push(v);
                }
            }
        }
        false
    }
}
