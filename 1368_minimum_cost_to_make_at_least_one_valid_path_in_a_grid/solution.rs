// LeetCode 1368 - Minimum Cost to Make at Least One Valid Path in a Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

use std::collections::VecDeque;

impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![i32::MAX / 2; n]; m];
        dist[0][0] = 0;
        let mut q = VecDeque::new();
        q.push_back((0usize, 0usize));
        let dirs = [(0i32, 1i32), (0, -1), (1, 0), (-1, 0)];
        while let Some((r, c)) = q.pop_front() {
            for (k, &(dr, dc)) in dirs.iter().enumerate() {
                let x = r as i32 + dr;
                let y = c as i32 + dc;
                if x >= 0 && (x as usize) < m && y >= 0 && (y as usize) < n {
                    let w = i32::from(k as i32 + 1 != grid[r][c]);
                    let nd = dist[r][c] + w;
                    let (xu, yu) = (x as usize, y as usize);
                    if nd < dist[xu][yu] {
                        dist[xu][yu] = nd;
                        if w == 0 {
                            q.push_front((xu, yu));
                        } else {
                            q.push_back((xu, yu));
                        }
                    }
                }
            }
        }
        dist[m - 1][n - 1]
    }
}
