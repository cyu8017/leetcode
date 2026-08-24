struct Solution;

// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

use std::collections::HashSet;

impl Solution {
    pub fn root_count(edges: Vec<Vec<i32>>, guesses: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let guess_set: HashSet<(usize, usize)> = guesses
            .into_iter()
            .map(|gu| (gu[0] as usize, gu[1] as usize))
            .collect();
        fn dfs1(u: usize, p: i32, g: &[Vec<usize>], guess_set: &HashSet<(usize, usize)>) -> i32 {
            let mut cnt = 0;
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if guess_set.contains(&(u, v)) {
                    cnt += 1;
                }
                cnt += dfs1(v, u as i32, g, guess_set);
            }
            cnt
        }
        let base = dfs1(0, -1, &g, &guess_set);
        let mut ans = 0;
        fn dfs2(
            u: usize,
            p: i32,
            cur: i32,
            k: i32,
            g: &[Vec<usize>],
            guess_set: &HashSet<(usize, usize)>,
            ans: &mut i32,
        ) {
            if cur >= k {
                *ans += 1;
            }
            for &v in &g[u] {
                if v as i32 == p {
                    continue;
                }
                let mut nxt = cur;
                if guess_set.contains(&(u, v)) {
                    nxt -= 1;
                }
                if guess_set.contains(&(v, u)) {
                    nxt += 1;
                }
                dfs2(v, u as i32, nxt, k, g, guess_set, ans);
            }
        }
        dfs2(0, -1, base, k, &g, &guess_set, &mut ans);
        ans
    }
}

fn main() {}
