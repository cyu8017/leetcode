// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

use std::collections::HashSet;

impl Solution {
    pub fn max_weight(n: i32, edges: Vec<Vec<i32>>, k: i32, t: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mut graph = vec![Vec::<(usize, i32)>::new(); n];
        for e in &edges {
            graph[e[0] as usize].push((e[1] as usize, e[2]));
        }
        let mut dp = vec![vec![HashSet::<i32>::new(); k + 1]; n];
        for u in 0..n {
            dp[u][0].insert(0);
        }
        for i in 0..k {
            for u in 0..n {
                let sums: Vec<i32> = dp[u][i].iter().copied().collect();
                for sum in sums {
                    for &(to, w) in &graph[u] {
                        let ns = sum + w;
                        if ns < t {
                            dp[to][i + 1].insert(ns);
                        }
                    }
                }
            }
        }
        let mut ans = -1;
        for u in 0..n {
            for &sum in &dp[u][k] {
                if sum > ans {
                    ans = sum;
                }
            }
        }
        ans
    }
}
