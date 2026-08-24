// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

use std::collections::HashMap;

impl Solution {
    pub fn sum_of_ancestors(n: i32, edges: Vec<Vec<i32>>, nums: Vec<i32>) -> i64 {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            graph[u].push(v);
            graph[v].push(u);
        }
        fn kernel(mut x: i32) -> i32 {
            let mut res = 1;
            let mut p = 2;
            while p * p <= x {
                let mut cnt = 0;
                while x % p == 0 {
                    x /= p;
                    cnt += 1;
                }
                if cnt % 2 == 1 {
                    res *= p;
                }
                p += 1;
            }
            if x > 1 {
                res *= x;
            }
            res
        }
        let ks: Vec<i32> = nums.into_iter().map(kernel).collect();
        let mut freq = HashMap::new();
        let mut ans = 0i64;
        fn dfs(
            u: usize,
            p: i32,
            graph: &[Vec<usize>],
            ks: &[i32],
            freq: &mut HashMap<i32, i32>,
            ans: &mut i64,
        ) {
            *ans += *freq.get(&ks[u]).unwrap_or(&0) as i64;
            *freq.entry(ks[u]).or_insert(0) += 1;
            for &v in &graph[u] {
                if v as i32 != p {
                    dfs(v, u as i32, graph, ks, freq, ans);
                }
            }
            *freq.entry(ks[u]).or_insert(0) -= 1;
        }
        dfs(0, -1, &graph, &ks, &mut freq, &mut ans);
        ans
    }
}
