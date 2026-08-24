// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_obstacles(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![i32::MAX / 2; n]; m];
        dist[0][0] = 0;
        let mut dq = VecDeque::new();
        dq.push_back((0usize, 0usize));
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c)) = dq.pop_front() {
            for &(dr, dc) in &dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                let nd = dist[r][c] + grid[nr][nc];
                if nd < dist[nr][nc] {
                    dist[nr][nc] = nd;
                    if grid[nr][nc] == 0 {
                        dq.push_front((nr, nc));
                    } else {
                        dq.push_back((nr, nc));
                    }
                }
            }
        }
        dist[m - 1][n - 1]
    }
}
