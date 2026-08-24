// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

impl Solution {
    pub fn count_pairs_of_connectable_servers(edges: Vec<Vec<i32>>, signal_speed: i32) -> Vec<i32> {
        let n = edges.len() + 1;
        let mut g = vec![Vec::new(); n];
        for e in &edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        fn dfs(g: &[Vec<(usize, i32)>], a: usize, fa: usize, ws: i32, signal_speed: i32) -> i32 {
            let mut cnt = if ws % signal_speed == 0 { 1 } else { 0 };
            for &(b, w) in &g[a] {
                if b != fa {
                    cnt += dfs(g, b, a, ws + w, signal_speed);
                }
            }
            cnt
        }
        let mut ans = vec![0; n];
        for a in 0..n {
            let mut s = 0;
            for &(b, w) in &g[a] {
                let t = dfs(&g, b, a, w, signal_speed);
                ans[a] += s * t;
                s += t;
            }
        }
        ans
    }
}
