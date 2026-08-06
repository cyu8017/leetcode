// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

use std::collections::HashSet;

impl Solution {
    pub fn contains_cycle(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let mut seen = HashSet::new();

        fn dfs(
            r: i32,
            c: i32,
            pr: i32,
            pc: i32,
            grid: &[Vec<char>],
            m: usize,
            n: usize,
            seen: &mut HashSet<(i32, i32)>,
        ) -> bool {
            seen.insert((r, c));
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                let nr = r + dr;
                let nc = c + dc;
                if nr < 0
                    || nc < 0
                    || nr as usize >= m
                    || nc as usize >= n
                    || grid[nr as usize][nc as usize] != grid[r as usize][c as usize]
                    || (nr == pr && nc == pc)
                {
                    continue;
                }
                if seen.contains(&(nr, nc)) || dfs(nr, nc, r, c, grid, m, n, seen) {
                    return true;
                }
            }
            false
        }

        for r in 0..m {
            for c in 0..n {
                if !seen.contains(&(r as i32, c as i32))
                    && dfs(r as i32, c as i32, -1, -1, &grid, m, n, &mut seen)
                {
                    return true;
                }
            }
        }
        false
    }
}
