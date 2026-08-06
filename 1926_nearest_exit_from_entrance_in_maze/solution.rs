// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

use std::collections::VecDeque;

impl Solution {
    pub fn nearest_exit(mut maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        let m = maze.len();
        let n = maze[0].len();
        let er = entrance[0] as usize;
        let ec = entrance[1] as usize;
        let mut q = VecDeque::new();
        q.push_back((er, ec, 0));
        maze[er][ec] = '+';
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c, d)) = q.pop_front() {
            for &(dr, dc) in &dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if maze[nr][nc] == '.' {
                        if nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1 {
                            return d + 1;
                        }
                        maze[nr][nc] = '+';
                        q.push_back((nr, nc, d + 1));
                    }
                }
            }
        }
        -1
    }
}
