// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

use std::collections::{HashSet, VecDeque};

impl Solution {
    fn expand_pal(g: &[Vec<usize>], label: &[u8], l: usize, r: usize) -> i32 {
        let mut vis: HashSet<(usize, usize)> = HashSet::new();
        let mut q: VecDeque<(usize, usize, i32)> = VecDeque::new();
        let len0 = if l != r { 2 } else { 1 };
        q.push_back((l, r, len0));
        let mut best = len0;
        vis.insert((l.min(r), l.max(r)));
        while let Some((cl, cr, length)) = q.pop_front() {
            for &a in &g[cl] {
                for &b in &g[cr] {
                    if a == b || label[a] != label[b] {
                        continue;
                    }
                    let p = (a.min(b), a.max(b));
                    if vis.contains(&p) {
                        continue;
                    }
                    vis.insert(p);
                    let nl = length + 2;
                    best = best.max(nl);
                    q.push_back((a, b, nl));
                }
            }
        }
        best
    }

    pub fn max_len(n: i32, edges: Vec<Vec<i32>>, label: String) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            g[u].push(v);
            g[v].push(u);
        }
        let label = label.into_bytes();
        let mut ans = 1;
        for i in 0..n {
            ans = ans.max(Self::expand_pal(&g, &label, i, i));
            for &j in &g[i] {
                if i < j && label[i] == label[j] {
                    ans = ans.max(Self::expand_pal(&g, &label, i, j));
                }
            }
        }
        ans
    }
}
