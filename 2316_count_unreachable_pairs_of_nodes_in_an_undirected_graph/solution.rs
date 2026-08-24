// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

impl Solution {
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut vis = vec![false; n];
        fn dfs(u: usize, g: &[Vec<usize>], vis: &mut [bool]) -> i64 {
            vis[u] = true;
            let mut size = 1i64;
            for &v in &g[u] {
                if !vis[v] {
                    size += dfs(v, g, vis);
                }
            }
            size
        }
        let mut ans = 0i64;
        let mut seen = 0i64;
        for i in 0..n {
            if !vis[i] {
                let sz = dfs(i, &g, &mut vis);
                ans += sz * seen;
                seen += sz;
            }
        }
        ans
    }
}
