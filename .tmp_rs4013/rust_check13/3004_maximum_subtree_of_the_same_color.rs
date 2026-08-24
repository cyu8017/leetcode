#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3004 - Maximum Subtree of the Same Color
// https://leetcode.com/problems/maximum-subtree-of-the-same-color/

impl Solution {
    pub fn maximum_subtree_size(edges: Vec<Vec<i32>>, colors: Vec<i32>) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut size = vec![0; n];
        let mut ans = 0;
        fn dfs(
            a: usize,
            fa: i32,
            g: &[Vec<usize>],
            colors: &[i32],
            size: &mut [i32],
            ans: &mut i32,
        ) -> bool {
            size[a] = 1;
            let mut ok = true;
            for &b in &g[a] {
                if b as i32 != fa {
                    let t = dfs(b, a as i32, g, colors, size, ans);
                    ok = ok && t && colors[a] == colors[b];
                    size[a] += size[b];
                }
            }
            if ok {
                *ans = (*ans).max(size[a]);
            }
            ok
        }
        dfs(0, -1, &g, &colors, &mut size, &mut ans);
        ans
    }
}
