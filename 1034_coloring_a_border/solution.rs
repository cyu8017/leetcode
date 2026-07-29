// LeetCode 1034 - Coloring A Border
// https://leetcode.com/problems/coloring-a-border/

use std::collections::HashSet;

impl Solution {
    pub fn color_border(mut grid: Vec<Vec<i32>>, row: i32, col: i32, color: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let original = grid[row as usize][col as usize];
        let mut component = HashSet::new();
        let mut stack = vec![(row as usize, col as usize)];
        component.insert((row as usize, col as usize));
        while let Some((r, c)) = stack.pop() {
            for (nr, nc) in [
                (r.wrapping_add(1), c),
                (r.wrapping_sub(1), c),
                (r, c.wrapping_add(1)),
                (r, c.wrapping_sub(1)),
            ] {
                if nr < m && nc < n && grid[nr][nc] == original && component.insert((nr, nc)) {
                    stack.push((nr, nc));
                }
            }
        }
        let mut border = Vec::new();
        for &(r, c) in &component {
            let is_border = [
                (r as isize + 1, c as isize),
                (r as isize - 1, c as isize),
                (r as isize, c as isize + 1),
                (r as isize, c as isize - 1),
            ]
            .iter()
            .any(|&(nr, nc)| {
                nr < 0
                    || nc < 0
                    || nr >= m as isize
                    || nc >= n as isize
                    || !component.contains(&(nr as usize, nc as usize))
            });
            if is_border {
                border.push((r, c));
            }
        }
        for (r, c) in border {
            grid[r][c] = color;
        }
        grid
    }
}
