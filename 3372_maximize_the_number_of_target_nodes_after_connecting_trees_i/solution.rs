// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

use std::collections::VecDeque;

impl Solution {
    fn build_tree(n: usize, edges: &[Vec<i32>]) -> Vec<Vec<usize>> {
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        g
    }

    fn count_within(g: &[Vec<usize>], start: usize, k: i32) -> i32 {
        if k < 0 {
            return 0;
        }
        let n = g.len();
        let mut vis = vec![false; n];
        let mut q = VecDeque::new();
        q.push_back((start, 0));
        vis[start] = true;
        let mut cnt = 0;
        while let Some((u, d)) = q.pop_front() {
            cnt += 1;
            if d == k {
                continue;
            }
            for &v in &g[u] {
                if !vis[v] {
                    vis[v] = true;
                    q.push_back((v, d + 1));
                }
            }
        }
        cnt
    }

    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let n = edges1.len() + 1;
        let m = edges2.len() + 1;
        let g1 = Self::build_tree(n, &edges1);
        let g2 = Self::build_tree(m, &edges2);
        let mut cnt1 = vec![0; n];
        for i in 0..n {
            cnt1[i] = Self::count_within(&g1, i, k);
        }
        let mut best2 = 0;
        if k > 0 {
            for i in 0..m {
                let c = Self::count_within(&g2, i, k - 1);
                if c > best2 {
                    best2 = c;
                }
            }
        }
        (0..n).map(|i| cnt1[i] + best2).collect()
    }
}
