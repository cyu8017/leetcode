// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

use std::collections::VecDeque;

impl Solution {
    pub fn find_median(n: i32, edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::<(usize, i32)>::new(); n];
        for e in &edges {
            let (u, v, w) = (e[0] as usize, e[1] as usize, e[2]);
            g[u].push((v, w));
            g[v].push((u, w));
        }
        let mut ans = vec![0; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            let (u, v) = (q[0] as usize, q[1] as usize);
            let mut parent = vec![-2i32; n];
            let mut pw = vec![0i32; n];
            parent[u] = -1;
            let mut qq = VecDeque::new();
            qq.push_back(u);
            while let Some(x) = qq.pop_front() {
                if x == v {
                    break;
                }
                for &(to, w) in &g[x] {
                    if parent[to] == -2 {
                        parent[to] = x as i32;
                        pw[to] = w;
                        qq.push_back(to);
                    }
                }
            }
            let mut nodes = vec![v];
            let mut weights = Vec::new();
            let mut cur = v;
            while cur != u {
                weights.push(pw[cur]);
                cur = parent[cur] as usize;
                nodes.push(cur);
            }
            nodes.reverse();
            weights.reverse();
            let total: i32 = weights.iter().sum();
            let need = (total + 1) / 2;
            let mut sum = 0;
            let mut med = u as i32;
            for i in 0..weights.len() {
                sum += weights[i];
                med = nodes[i + 1] as i32;
                if sum >= need {
                    break;
                }
            }
            ans[qi] = med;
        }
        ans
    }
}
