struct Solution;
// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

impl Solution {
    pub fn min_edge_reversals(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in edges {
            let u = e[0] as usize;
            let v = e[1] as usize;
            g[u].push((v, 0i32));
            g[v].push((u, 1i32));
        }
        let mut ans = vec![0i32; n];
        fn dfs1(u: usize, p: i32, g: &[Vec<(usize, i32)>], ans: &mut [i32]) {
            for &(v, ww) in &g[u] {
                if v as i32 == p {
                    continue;
                }
                ans[0] += ww;
                dfs1(v, u as i32, g, ans);
            }
        }
        fn dfs2(u: usize, p: i32, g: &[Vec<(usize, i32)>], ans: &mut [i32]) {
            for &(v, ww) in &g[u] {
                if v as i32 == p {
                    continue;
                }
                if ww == 0 {
                    ans[v] = ans[u] + 1;
                } else {
                    ans[v] = ans[u] - 1;
                }
                dfs2(v, u as i32, g, ans);
            }
        }
        dfs1(0, -1, &g, &mut ans);
        dfs2(0, -1, &g, &mut ans);
        ans
    }
}

fn main() {}
