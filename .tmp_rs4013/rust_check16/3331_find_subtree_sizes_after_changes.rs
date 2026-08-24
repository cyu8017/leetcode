struct Solution;
// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

impl Solution {
    pub fn find_subtree_sizes(parent: Vec<i32>, s: String) -> Vec<i32> {
        let n = parent.len();
        let mut g = vec![Vec::new(); n];
        for i in 1..n {
            g[parent[i] as usize].push(i);
        }
        let mut new_parent = parent.clone();
        let mut last = [-1i32; 26];
        let sb = s.as_bytes();
        fn dfs1(u: usize, g: &[Vec<usize>], sb: &[u8], last: &mut [i32; 26], new_parent: &mut [i32]) {
            let c = (sb[u] - b'a') as usize;
            let prev = last[c];
            if prev != -1 {
                new_parent[u] = prev;
            }
            last[c] = u as i32;
            for &v in &g[u] {
                dfs1(v, g, sb, last, new_parent);
            }
            last[c] = prev;
        }
        dfs1(0, &g, sb, &mut last, &mut new_parent);
        let mut ng = vec![Vec::new(); n];
        for i in 1..n {
            ng[new_parent[i] as usize].push(i);
        }
        let mut ans = vec![0; n];
        fn dfs2(u: usize, ng: &[Vec<usize>], ans: &mut [i32]) -> i32 {
            let mut sz = 1;
            for &v in &ng[u] {
                sz += dfs2(v, ng, ans);
            }
            ans[u] = sz;
            sz
        }
        dfs2(0, &ng, &mut ans);
        ans
    }
}

fn main() {}
