// LeetCode 0694 - Number of Distinct Islands
// https://leetcode.com/problems/number-of-distinct-islands/

use std::collections::HashSet;

impl Solution {
    pub fn num_distinct_islands(mut grid: Vec<Vec<i32>>) -> i32 {
        if grid.is_empty() {
            return 0;
        }
        let mut shapes = HashSet::new();
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if grid[i][j] == 1 {
                    let mut path = Vec::new();
                    Self::dfs(&mut grid, i as i32, j as i32, i as i32, j as i32, &mut path);
                    shapes.insert(path);
                }
            }
        }
        shapes.len() as i32
    }

    fn dfs(
        grid: &mut [Vec<i32>],
        r: i32,
        c: i32,
        br: i32,
        bc: i32,
        path: &mut Vec<(i32, i32)>,
    ) {
        if r < 0
            || r >= grid.len() as i32
            || c < 0
            || c >= grid[0].len() as i32
            || grid[r as usize][c as usize] == 0
        {
            return;
        }
        grid[r as usize][c as usize] = 0;
        path.push((r - br, c - bc));
        Self::dfs(grid, r + 1, c, br, bc, path);
        Self::dfs(grid, r - 1, c, br, bc, path);
        Self::dfs(grid, r, c + 1, br, bc, path);
        Self::dfs(grid, r, c - 1, br, bc, path);
    }
}
