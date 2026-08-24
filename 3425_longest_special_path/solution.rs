// LeetCode 3425 - Longest Special Path
// https://leetcode.com/problems/longest-special-path/

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
        let mut last = HashMap::new();
        fn dfs(
            u: usize,
            p: i32,
            dist: i32,
            left: usize,
            path: &mut Vec<i32>,
            g: &[Vec<(usize, i32)>],
            nums: &[i32],
            last: &mut HashMap<i32, usize>,
            best_len: &mut i32,
            best_nodes: &mut i32,
        ) {
            let seen = last.contains_key(&nums[u]);
            let prev_pos = if seen { last[&nums[u]] as i32 } else { -1 };
            last.insert(nums[u], path.len());
            let mut new_left = left;
            if seen && prev_pos >= left as i32 {
                new_left = (prev_pos + 1) as usize;
            }
            path.push(dist);
            let length = dist - path[new_left];
            let nodes = (path.len() - new_left) as i32;
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
                    new_left,
                    path,
                    g,
                    nums,
                    last,
                    best_len,
                    best_nodes,
                );
            }
            path.pop();
            if seen {
                last.insert(nums[u], prev_pos as usize);
            } else {
                last.remove(&nums[u]);
            }
        }
        let mut path = Vec::new();
        dfs(
            0,
            -1,
            0,
            0,
            &mut path,
            &g,
            &nums,
            &mut last,
            &mut best_len,
            &mut best_nodes,
        );
        vec![best_len, best_nodes]
    }
}
