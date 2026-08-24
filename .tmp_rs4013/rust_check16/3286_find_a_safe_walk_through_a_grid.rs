struct Solution;
// LeetCode 3286 - Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

use std::collections::VecDeque;

impl Solution {
    pub fn find_safe_walk(grid: Vec<Vec<i32>>, health: i32) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let mut vis = vec![vec![-1; n]; m];
        let qh = health - grid[0][0];
        if qh <= 0 {
            return false;
        }
        let mut q = VecDeque::new();
        q.push_back([0, 0, qh]);
        vis[0][0] = qh;
        const DIRS: [[i32; 2]; 4] = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        while let Some(cur) = q.pop_front() {
            if cur[0] == m as i32 - 1 && cur[1] == n as i32 - 1 {
                return true;
            }
            for d in &DIRS {
                let nr = cur[0] + d[0];
                let nc = cur[1] + d[1];
                if nr < 0 || nc < 0 || nr >= m as i32 || nc >= n as i32 {
                    continue;
                }
                let nh = cur[2] - grid[nr as usize][nc as usize];
                if nh <= 0 {
                    continue;
                }
                if nh > vis[nr as usize][nc as usize] {
                    vis[nr as usize][nc as usize] = nh;
                    q.push_back([nr, nc, nh]);
                }
            }
        }
        false
    }
}

fn main() {}
