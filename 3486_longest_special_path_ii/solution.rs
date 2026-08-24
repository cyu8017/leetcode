// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

use std::collections::HashMap;

impl Solution {
    pub fn longest_special_path(edges: Vec<Vec<i32>>, nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        let mut best_len = 0;
        let mut best_nodes = 1;
        fn dfs(
            u: usize,
            p: i32,
            dist: i32,
            path_vals: &mut Vec<i32>,
            path_dist: &mut Vec<i32>,
            g: &[Vec<(usize, i32)>],
            nums: &[i32],
            best_len: &mut i32,
            best_nodes: &mut i32,
        ) {
            path_vals.push(nums[u]);
            path_dist.push(dist);
            let mut freq = HashMap::new();
            let mut dups = 0;
            let mut left = 0;
            for right in 0..path_vals.len() {
                let e = freq.entry(path_vals[right]).or_insert(0);
                *e += 1;
                if *e == 2 {
                    dups += 1;
                }
                while dups > 1 {
                    if freq[&path_vals[left]] == 2 {
                        dups -= 1;
                    }
                    *freq.get_mut(&path_vals[left]).unwrap() -= 1;
                    left += 1;
                }
            }
            let length = dist - path_dist[left];
            let nodes = (path_vals.len() - left) as i32;
            if length > *best_len || (length == *best_len && nodes < *best_nodes) {
                *best_len = length;
                *best_nodes = nodes;
            }
            for &(to, w) in &g[u] {
                if to as i32 == p {
                    continue;
                }
                dfs(
                    to,
                    u as i32,
                    dist + w,
                    path_vals,
                    path_dist,
                    g,
                    nums,
                    best_len,
                    best_nodes,
                );
            }
            path_vals.pop();
            path_dist.pop();
        }
        let mut path_vals = Vec::new();
        let mut path_dist = Vec::new();
        dfs(
            0,
            -1,
            0,
            &mut path_vals,
            &mut path_dist,
            &g,
            &nums,
            &mut best_len,
            &mut best_nodes,
        );
        vec![best_len, best_nodes]
    }
}
