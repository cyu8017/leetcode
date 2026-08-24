// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

use std::collections::HashSet;

impl Solution {
    pub fn number_of_paths(n: i32, corridors: Vec<Vec<i32>>) -> i32 {
        let mut g = vec![HashSet::new(); n as usize + 1];
        for e in &corridors {
            g[e[0] as usize].insert(e[1]);
            g[e[1] as usize].insert(e[0]);
        }
        let mut ans = 0;
        for e in &corridors {
            let a = e[0] as usize;
            let b = e[1];
            for &c in &g[a] {
                if g[b as usize].contains(&c) {
                    ans += 1;
                }
            }
        }
        ans / 3
    }
}
