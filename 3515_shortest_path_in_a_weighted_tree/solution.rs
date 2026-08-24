// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

use std::collections::HashMap;

impl Solution {
    pub fn tree_queries(n: i32, edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::<(usize, i32)>::new(); n + 1];
        let mut weight: HashMap<(i32, i32), i32> = HashMap::new();
        for e in &edges {
            let (u, v, w) = (e[0] as usize, e[1] as usize, e[2]);
            g[u].push((v, w));
            g[v].push((u, w));
            let a = e[0].min(e[1]);
            let b = e[0].max(e[1]);
            weight.insert((a, b), w);
        }
        let mut in_t = vec![0i32; n + 1];
        let mut out_t = vec![0i32; n + 1];
        let mut dist = vec![0i32; n + 1];
        let mut parent = vec![0usize; n + 1];
        fn dfs(
            u: usize,
            p: usize,
            g: &[Vec<(usize, i32)>],
            in_t: &mut [i32],
            out_t: &mut [i32],
            dist: &mut [i32],
            parent: &mut [usize],
            time: &mut i32,
        ) {
            in_t[u] = *time;
            *time += 1;
            for &(to, w) in &g[u] {
                if to == p {
                    continue;
                }
                parent[to] = u;
                dist[to] = dist[u] + w;
                dfs(to, u, g, in_t, out_t, dist, parent, time);
            }
            out_t[u] = *time - 1;
        }
        let mut time = 0;
        dfs(1, 0, &g, &mut in_t, &mut out_t, &mut dist, &mut parent, &mut time);
        let mut bit = vec![0i32; n + 2];
        let add = |bit: &mut [i32], mut i: i32, v: i32| {
            while i <= n as i32 {
                bit[i as usize] += v;
                i += i & -i;
            }
        };
        let range_add = |bit: &mut [i32], l: i32, r: i32, v: i32| {
            add(bit, l + 1, v);
            add(bit, r + 2, -v);
        };
        let point = |bit: &[i32], mut i: i32| {
            let mut s = 0;
            i += 1;
            while i > 0 {
                s += bit[i as usize];
                i -= i & -i;
            }
            s
        };
        for i in 1..=n {
            range_add(&mut bit, in_t[i], in_t[i], dist[i]);
        }
        let mut ans = Vec::new();
        for q in queries {
            if q[0] == 1 {
                let u = q[1] as usize;
                let v = q[2] as usize;
                let nw = q[3];
                let a = q[1].min(q[2]);
                let b = q[1].max(q[2]);
                let ow = *weight.get(&(a, b)).unwrap();
                let delta = nw - ow;
                weight.insert((a, b), nw);
                let child = if parent[u] == v { u } else { v };
                range_add(&mut bit, in_t[child], out_t[child], delta);
            } else {
                ans.push(point(&bit, in_t[q[1] as usize]));
            }
        }
        ans
    }
}
