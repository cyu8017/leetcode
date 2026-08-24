// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

impl Solution {
    pub fn max_subgraph_score(n: i32, edges: Vec<Vec<i32>>, good: Vec<i32>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut parent = vec![-2i32; n];
        parent[0] = -1;
        let mut order = vec![0usize];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            for &v in &g[u] {
                if parent[v] == -2 {
                    parent[v] = u as i32;
                    order.push(v);
                }
            }
            i += 1;
        }
        let mut down = vec![0i32; n];
        for i in (0..n).rev() {
            let u = order[i];
            down[u] = 2 * good[u] - 1;
            for &v in &g[u] {
                if parent[v] == u as i32 && down[v] > 0 {
                    down[u] += down[v];
                }
            }
        }
        let mut ans = down.clone();
        for &u in &order {
            for &v in &g[u] {
                if parent[v] == u as i32 {
                    let mut outside = ans[u];
                    if down[v] > 0 {
                        outside -= down[v];
                    }
                    ans[v] = down[v];
                    if outside > 0 {
                        ans[v] += outside;
                    }
                }
            }
        }
        ans
    }
}
