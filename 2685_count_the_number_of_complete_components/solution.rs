// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

impl Solution {
    pub fn count_complete_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push(e[1] as usize);
            g[e[1] as usize].push(e[0] as usize);
        }
        let mut vis = vec![false; n];
        let mut ans = 0;
        for i in 0..n {
            if vis[i] {
                continue;
            }
            let mut nodes = Vec::new();
            fn dfs(u: usize, g: &[Vec<usize>], vis: &mut [bool], nodes: &mut Vec<usize>) {
                vis[u] = true;
                nodes.push(u);
                for &v in &g[u] {
                    if !vis[v] {
                        dfs(v, g, vis, nodes);
                    }
                }
            }
            dfs(i, &g, &mut vis, &mut nodes);
            let mut ecount = 0;
            for &u in &nodes {
                ecount += g[u].len() as i32;
            }
            ecount /= 2;
            let sz = nodes.len() as i32;
            if ecount == sz * (sz - 1) / 2 {
                ans += 1;
            }
        }
        ans
    }
}
