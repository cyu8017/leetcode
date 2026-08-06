// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

impl Solution {
    pub fn frog_position(n: i32, edges: Vec<Vec<i32>>, t: i32, target: i32) -> f64 {
        let n = n as usize;
        let mut g = vec![Vec::new(); n + 1];
        for e in edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            g[a].push(b);
            g[b].push(a);
        }
        fn dfs(u: usize, p: usize, time: i32, t: i32, target: usize, prob: f64, g: &[Vec<usize>]) -> f64 {
            let kids: Vec<usize> = g[u].iter().copied().filter(|&v| v != p).collect();
            if time == t || kids.is_empty() {
                return if u == target { prob } else { 0.0 };
            }
            kids.iter()
                .map(|&v| dfs(v, u, time + 1, t, target, prob / kids.len() as f64, g))
                .sum()
        }
        dfs(1, 0, 0, t, target as usize, 1.0, &g)
    }
}
