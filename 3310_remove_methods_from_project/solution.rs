// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

impl Solution {
    pub fn remaining_methods(n: i32, k: i32, invocations: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut g = vec![Vec::new(); n];
        for e in &invocations {
            g[e[0] as usize].push(e[1] as usize);
        }
        let mut sus = vec![false; n];
        fn dfs(u: usize, g: &[Vec<usize>], sus: &mut [bool]) {
            if sus[u] {
                return;
            }
            sus[u] = true;
            for &v in &g[u] {
                dfs(v, g, sus);
            }
        }
        dfs(k as usize, &g, &mut sus);
        for e in &invocations {
            if !sus[e[0] as usize] && sus[e[1] as usize] {
                return (0..n as i32).collect();
            }
        }
        (0..n as i32).filter(|&i| !sus[i as usize]).collect()
    }
}
