// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

use std::collections::VecDeque;

impl Solution {
    pub fn get_food(grid: Vec<Vec<char>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut queue: VecDeque<(usize, usize, i32)> = VecDeque::new();
        let mut seen = vec![vec![false; cols]; rows];
        for r in 0..rows {
            for c in 0..cols {
                if grid[r][c] == '*' {
                    queue.push_back((r, c, 0));
                    seen[r][c] = true;
                }
            }
        }
        let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c, d)) = queue.pop_front() {
            if grid[r][c] == '#' {
                return d;
            }
            for &(dr, dc) in &dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < rows as i32 && nc >= 0 && nc < cols as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if !seen[nr][nc] && grid[nr][nc] != 'X' {
                        seen[nr][nc] = true;
                        queue.push_back((nr, nc, d + 1));
                    }
                }
            }
        }
        -1
    }
}
