// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

use std::collections::HashSet;

impl Solution {
    pub fn garden_no_adj(n: i32, paths: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n + 1];
        for p in paths {
            let (a, b) = (p[0] as usize, p[1] as usize);
            graph[a].push(b);
            graph[b].push(a);
        }
        let mut ans = vec![0; n + 1];
        for garden in 1..=n {
            let used: HashSet<i32> = graph[garden].iter().map(|&nei| ans[nei]).collect();
            ans[garden] = (1..=4).find(|c| !used.contains(c)).unwrap();
        }
        ans[1..].to_vec()
    }
}
