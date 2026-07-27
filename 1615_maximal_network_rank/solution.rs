// LeetCode 1615 - Maximal Network Rank
// https://leetcode.com/problems/maximal-network-rank/

use std::collections::HashSet;

impl Solution {
    pub fn maximal_network_rank(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut degree = vec![0i32; n];
        let mut edges = HashSet::new();
        for r in roads {
            let (mut a, mut b) = (r[0] as usize, r[1] as usize);
            degree[a] += 1;
            degree[b] += 1;
            if a > b {
                std::mem::swap(&mut a, &mut b);
            }
            edges.insert((a, b));
        }
        let mut ans = 0;
        for a in 0..n {
            for b in a + 1..n {
                let mut cur = degree[a] + degree[b];
                if edges.contains(&(a, b)) {
                    cur -= 1;
                }
                ans = ans.max(cur);
            }
        }
        ans
    }
}
