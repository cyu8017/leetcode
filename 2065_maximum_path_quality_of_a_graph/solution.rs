// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

impl Solution {
    pub fn maximal_path_quality(values: Vec<i32>, edges: Vec<Vec<i32>>, max_time: i32) -> i32 {
        let n = values.len();
        let mut g = vec![Vec::new(); n];
        for e in edges {
            g[e[0] as usize].push((e[1] as usize, e[2]));
            g[e[1] as usize].push((e[0] as usize, e[2]));
        }
        fn dfs(
            u: usize,
            time: i32,
            quality: i32,
            max_time: i32,
            values: &[i32],
            g: &[Vec<(usize, i32)>],
            vis: &mut [i32],
            ans: &mut i32,
        ) {
            if time > max_time {
                return;
            }
            let first = vis[u] == 0;
            let quality = if first { quality + values[u] } else { quality };
            vis[u] += 1;
            if u == 0 {
                *ans = (*ans).max(quality);
            }
            for &(v, w) in &g[u] {
                dfs(v, time + w, quality, max_time, values, g, vis, ans);
            }
            vis[u] -= 1;
        }
        let mut vis = vec![0; n];
        let mut ans = 0;
        dfs(0, 0, 0, max_time, &values, &g, &mut vis, &mut ans);
        ans
    }
}
