// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

impl Solution {
    pub fn longest_path(parent: Vec<i32>, s: String) -> i32 {
        let n = parent.len();
        let mut g = vec![Vec::new(); n];
        for i in 1..n {
            g[parent[i] as usize].push(i);
        }
        let s = s.into_bytes();
        let mut ans = 1;
        fn dfs(u: usize, g: &[Vec<usize>], s: &[u8], ans: &mut i32) -> i32 {
            let mut best1 = 0;
            let mut best2 = 0;
            for &v in &g[u] {
                let len_v = dfs(v, g, s, ans);
                if s[v] == s[u] {
                    continue;
                }
                if len_v > best1 {
                    best2 = best1;
                    best1 = len_v;
                } else if len_v > best2 {
                    best2 = len_v;
                }
            }
            *ans = (*ans).max(1 + best1 + best2);
            1 + best1
        }
        dfs(0, &g, &s, &mut ans);
        ans
    }
}
