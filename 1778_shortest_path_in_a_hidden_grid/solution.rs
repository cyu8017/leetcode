// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

use std::collections::VecDeque;

impl Solution {
    pub fn find_shortest_path(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut start = (0usize, 0usize);
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == -1 {
                    start = (i, j);
                }
            }
        }
        let dirs: [(i32, i32); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        let mut dist = vec![vec![-1i32; n]; m];
        let mut queue = VecDeque::new();
        dist[start.0][start.1] = 0;
        queue.push_back(start);
        while let Some((r, c)) = queue.pop_front() {
            if grid[r][c] == 2 {
                return dist[r][c];
            }
            for &(dr, dc) in &dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if grid[nr][nc] != 0 && dist[nr][nc] < 0 {
                        dist[nr][nc] = dist[r][c] + 1;
                        queue.push_back((nr, nc));
                    }
                }
            }
        }
        -1
    }
}
