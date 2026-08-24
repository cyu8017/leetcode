// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

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

    fn bipartite_count(g: &[Vec<usize>], color: &mut [i32]) -> [i32; 2] {
        color.fill(-1);
        let mut q = VecDeque::new();
        q.push_back(0);
        color[0] = 0;
        let mut cnt = [1, 0];
        while let Some(u) = q.pop_front() {
            for &v in &g[u] {
                if color[v] == -1 {
                    color[v] = color[u] ^ 1;
                    cnt[color[v] as usize] += 1;
                    q.push_back(v);
                }
            }
        }
        cnt
    }

    pub fn max_target_nodes(edges1: Vec<Vec<i32>>, edges2: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges1.len() + 1;
        let m = edges2.len() + 1;
        let g1 = Self::build_tree(n, &edges1);
        let g2 = Self::build_tree(m, &edges2);
        let mut color1 = vec![0; n];
        let mut color2 = vec![0; m];
        let c1 = Self::bipartite_count(&g1, &mut color1);
        let c2 = Self::bipartite_count(&g2, &mut color2);
        let best2 = c2[0].max(c2[1]);
        (0..n).map(|i| c1[color1[i] as usize] + best2).collect()
    }
}
