// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

impl Solution {
    pub fn min_increase(n: i32, edges: Vec<Vec<i32>>, cost: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut graph = vec![Vec::<usize>::new(); n];
        for e in &edges {
            graph[e[0] as usize].push(e[1] as usize);
            graph[e[1] as usize].push(e[0] as usize);
        }
        fn dfs(u: usize, p: i32, graph: &[Vec<usize>], cost: &[i32], ans: &mut i32) -> i64 {
            if graph[u].len() == 1 && p != -1 {
                return cost[u] as i64;
            }
            let mut child_vals = Vec::new();
            for &v in &graph[u] {
                if v as i32 == p {
                    continue;
                }
                child_vals.push(dfs(v, u as i32, graph, cost, ans));
            }
            if child_vals.is_empty() {
                return cost[u] as i64;
            }
            let mx = *child_vals.iter().max().unwrap();
            for c in child_vals {
                if c < mx {
                    *ans += 1;
                }
            }
            mx + cost[u] as i64
        }
        let mut ans = 0;
        dfs(0, -1, &graph, &cost, &mut ans);
        ans
    }
}
