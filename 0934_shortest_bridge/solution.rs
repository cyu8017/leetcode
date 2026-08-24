// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

use std::collections::VecDeque;

impl Solution {
    pub fn shortest_bridge(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        fn dfs(grid: &mut [Vec<i32>], r: i32, c: i32, n: i32, dirs: &[(i32, i32); 4]) {
            if r < 0 || r >= n || c < 0 || c >= n || grid[r as usize][c as usize] != 1 {
                return;
            }
            grid[r as usize][c as usize] = 2;
            for &(dr, dc) in dirs {
                dfs(grid, r + dr, c + dc, n, dirs);
            }
        }
        let mut found = false;
        for i in 0..n {
            if found {
                break;
            }
            for j in 0..n {
                if grid[i][j] == 1 {
                    dfs(&mut grid, i as i32, j as i32, n as i32, &dirs);
                    found = true;
                    break;
                }
            }
        }
        let mut q = VecDeque::new();
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 2 {
                    q.push_back((i as i32, j as i32, 0));
                }
            }
        }
        while let Some((r, c, dist)) = q.pop_front() {
            for &(dr, dc) in &dirs {
                let nr = r + dr;
                let nc = c + dc;
                if nr < 0 || nr >= n as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                if grid[nr as usize][nc as usize] == 1 {
                    return dist;
                }
                if grid[nr as usize][nc as usize] == 0 {
                    grid[nr as usize][nc as usize] = 2;
                    q.push_back((nr, nc, dist + 1));
                }
            }
        }
        -1
    }
}
