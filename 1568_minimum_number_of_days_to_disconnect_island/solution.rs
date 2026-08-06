// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

use std::collections::HashSet;

impl Solution {
    pub fn min_days(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        fn islands(grid: &[Vec<i32>], m: usize, n: usize) -> i32 {
            let mut seen = HashSet::new();
            let mut count = 0;
            for r in 0..m {
                for c in 0..n {
                    if grid[r][c] == 1 && !seen.contains(&(r, c)) {
                        count += 1;
                        let mut stack = vec![(r, c)];
                        seen.insert((r, c));
                        while let Some((x, y)) = stack.pop() {
                            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                                let nx = x as i32 + dx;
                                let ny = y as i32 + dy;
                                if nx >= 0
                                    && ny >= 0
                                    && (nx as usize) < m
                                    && (ny as usize) < n
                                    && grid[nx as usize][ny as usize] == 1
                                    && !seen.contains(&(nx as usize, ny as usize))
                                {
                                    seen.insert((nx as usize, ny as usize));
                                    stack.push((nx as usize, ny as usize));
                                }
                            }
                        }
                    }
                }
            }
            count
        }

        if islands(&grid, m, n) != 1 {
            return 0;
        }
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 1 {
                    grid[r][c] = 0;
                    if islands(&grid, m, n) != 1 {
                        grid[r][c] = 1;
                        return 1;
                    }
                    grid[r][c] = 1;
                }
            }
        }
        2
    }
}
