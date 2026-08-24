// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

use std::collections::HashSet;

impl Solution {
    pub fn num_distinct_islands2(mut grid: Vec<Vec<i32>>) -> i32 {
        if grid.is_empty() {
            return 0;
        }
        let m = grid.len();
        let n = grid[0].len();
        let mut shapes = HashSet::new();
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    let mut cells = Vec::new();
                    Self::dfs(&mut grid, i as i32, j as i32, m as i32, n as i32, &mut cells);
                    shapes.insert(Self::canonical(&cells));
                }
            }
        }
        shapes.len() as i32
    }

    fn dfs(
        grid: &mut [Vec<i32>],
        r: i32,
        c: i32,
        m: i32,
        n: i32,
        cells: &mut Vec<(i32, i32)>,
    ) {
        if r < 0 || r >= m || c < 0 || c >= n || grid[r as usize][c as usize] == 0 {
            return;
        }
        grid[r as usize][c as usize] = 0;
        cells.push((r, c));
        for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
            Self::dfs(grid, r + dr, c + dc, m, n, cells);
        }
    }

    fn canonical(cells: &[(i32, i32)]) -> Vec<(i32, i32)> {
        let transforms: [fn(i32, i32) -> (i32, i32); 8] = [
            |x, y| (x, y),
            |x, y| (x, -y),
            |x, y| (-x, y),
            |x, y| (-x, -y),
            |x, y| (y, x),
            |x, y| (y, -x),
            |x, y| (-y, x),
            |x, y| (-y, -x),
        ];
        let mut norms = Vec::new();
        for transform in transforms {
            let mut pts: Vec<(i32, i32)> = cells.iter().map(|&(x, y)| transform(x, y)).collect();
            let min_x = pts.iter().map(|p| p.0).min().unwrap();
            let min_y = pts.iter().map(|p| p.1).min().unwrap();
            for p in &mut pts {
                p.0 -= min_x;
                p.1 -= min_y;
            }
            pts.sort_unstable();
            norms.push(pts);
        }
        norms.into_iter().min().unwrap()
    }
}
