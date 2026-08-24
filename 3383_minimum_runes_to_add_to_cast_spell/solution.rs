// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

impl Solution {
    pub fn min_runes_to_add(n: i32, crystals: Vec<i32>, flow_from: Vec<i32>, flow_to: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        let mut rg = vec![Vec::new(); n];
        for i in 0..flow_from.len() {
            let a = flow_from[i] as usize;
            let b = flow_to[i] as usize;
            g[a].push(b);
            rg[b].push(a);
        }
        let mut vis = vec![false; n];
        let mut order = Vec::new();
        fn dfs1(u: usize, g: &[Vec<usize>], vis: &mut [bool], order: &mut Vec<usize>) {
            vis[u] = true;
            for &v in &g[u] {
                if !vis[v] {
                    dfs1(v, g, vis, order);
                }
            }
            order.push(u);
        }
        for i in 0..n {
            if !vis[i] {
                dfs1(i, &g, &mut vis, &mut order);
            }
        }
        let mut comp = vec![-1i32; n];
        let mut cid = 0i32;
        fn dfs2(u: usize, rg: &[Vec<usize>], comp: &mut [i32], cid: i32) {
            comp[u] = cid;
            for &v in &rg[u] {
                if comp[v] == -1 {
                    dfs2(v, rg, comp, cid);
                }
            }
        }
        for i in (0..n).rev() {
            let u = order[i];
            if comp[u] == -1 {
                dfs2(u, &rg, &mut comp, cid);
                cid += 1;
            }
        }
        let mut has_crystal = vec![false; cid as usize];
        for c in crystals {
            has_crystal[comp[c as usize] as usize] = true;
        }
        let mut indeg = vec![0; cid as usize];
        for u in 0..n {
            for &v in &g[u] {
                if comp[u] != comp[v] {
                    indeg[comp[v] as usize] += 1;
                }
            }
        }
        let mut ans = 0;
        for i in 0..cid as usize {
            if indeg[i] == 0 && !has_crystal[i] {
                ans += 1;
            }
        }
        ans
    }
}
