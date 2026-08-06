// LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn shortest_path(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        if k as usize >= m + n - 2 {
            return (m + n - 2) as i32;
        }
        let mut q = VecDeque::new();
        q.push_back((0usize, 0usize, k, 0i32));
        let mut best = HashMap::new();
        best.insert((0usize, 0usize), k);
        while let Some((r, c, rem, dist)) = q.pop_front() {
            if r == m - 1 && c == n - 1 {
                return dist;
            }
            for (dr, dc) in [(1isize, 0), (-1, 0), (0, 1), (0, -1)] {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                    let nr = nr as usize;
                    let nc = nc as usize;
                    let nxt = rem - grid[nr][nc];
                    let key = (nr, nc);
                    if nxt >= 0 && nxt > *best.get(&key).unwrap_or(&-1) {
                        best.insert(key, nxt);
                        q.push_back((nr, nc, nxt, dist + 1));
                    }
                }
            }
        }
        -1
    }
}
