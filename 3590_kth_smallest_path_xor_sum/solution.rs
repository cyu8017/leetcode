// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

impl Solution {
    pub fn kth_smallest(par: Vec<i32>, vals: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = par.len();
        let mut g = vec![Vec::<usize>::new(); n];
        for i in 1..n {
            g[par[i] as usize].push(i);
        }
        let mut xor_path = vec![0i32; n];
        fn dfs(u: usize, g: &[Vec<usize>], vals: &[i32], xor_path: &mut [i32]) {
            xor_path[u] ^= vals[u];
            for &v in &g[u] {
                xor_path[v] = xor_path[u];
                dfs(v, g, vals, xor_path);
            }
        }
        dfs(0, &g, &vals, &mut xor_path);
        let mut in_t = vec![0usize; n];
        let mut out_t = vec![0usize; n];
        let mut order = Vec::new();
        fn dfs2(u: usize, g: &[Vec<usize>], xor_path: &[i32], in_t: &mut [usize], out_t: &mut [usize], order: &mut Vec<i32>) {
            in_t[u] = order.len();
            order.push(xor_path[u]);
            for &v in &g[u] {
                dfs2(v, g, xor_path, in_t, out_t, order);
            }
            out_t[u] = order.len();
        }
        dfs2(0, &g, &xor_path, &mut in_t, &mut out_t, &mut order);
        queries
            .iter()
            .map(|q| {
                let u = q[0] as usize;
                let k = q[1] as usize;
                let mut sub = order[in_t[u]..out_t[u]].to_vec();
                sub.sort();
                sub.dedup();
                if k > sub.len() {
                    -1
                } else {
                    sub[k - 1]
                }
            })
            .collect()
    }
}
