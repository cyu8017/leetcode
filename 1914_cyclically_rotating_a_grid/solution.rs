// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

impl Solution {
    pub fn rotate_grid(mut grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let layers = m.min(n) / 2;
        for layer in 0..layers {
            let mut vals = Vec::new();
            for c in layer..n - layer {
                vals.push(grid[layer][c]);
            }
            for r in layer + 1..m - layer {
                vals.push(grid[r][n - layer - 1]);
            }
            if m - 2 * layer > 1 {
                for c in (layer..n - layer - 1).rev() {
                    vals.push(grid[m - layer - 1][c]);
                }
            }
            if n - 2 * layer > 1 {
                for r in (layer + 1..m - layer - 1).rev() {
                    vals.push(grid[r][layer]);
                }
            }
            let shift = (k as usize) % vals.len();
            vals.rotate_left(shift);
            let mut idx = 0;
            for c in layer..n - layer {
                grid[layer][c] = vals[idx];
                idx += 1;
            }
            for r in layer + 1..m - layer {
                grid[r][n - layer - 1] = vals[idx];
                idx += 1;
            }
            if m - 2 * layer > 1 {
                for c in (layer..n - layer - 1).rev() {
                    grid[m - layer - 1][c] = vals[idx];
                    idx += 1;
                }
            }
            if n - 2 * layer > 1 {
                for r in (layer + 1..m - layer - 1).rev() {
                    grid[r][layer] = vals[idx];
                    idx += 1;
                }
            }
        }
        grid
    }
}
