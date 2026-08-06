// LeetCode 1391 - Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

use std::collections::HashSet;

impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<i32>>) -> bool {
        let dirs: [&[(i32, i32)]; 7] = [
            &[],
            &[(0, -1), (0, 1)],
            &[(-1, 0), (1, 0)],
            &[(0, -1), (1, 0)],
            &[(0, 1), (1, 0)],
            &[(0, -1), (-1, 0)],
            &[(0, 1), (-1, 0)],
        ];
        let m = grid.len() as i32;
        let n = grid[0].len() as i32;
        let mut seen = HashSet::new();
        seen.insert((0, 0));
        let mut st = vec![(0i32, 0i32)];
        while let Some((r, c)) = st.pop() {
            if (r, c) == (m - 1, n - 1) {
                return true;
            }
            let t = grid[r as usize][c as usize] as usize;
            for &(dr, dc) in dirs[t] {
                let (x, y) = (r + dr, c + dc);
                if x >= 0
                    && x < m
                    && y >= 0
                    && y < n
                    && !seen.contains(&(x, y))
                    && dirs[grid[x as usize][y as usize] as usize]
                        .iter()
                        .any(|&(a, b)| a == -dr && b == -dc)
                {
                    seen.insert((x, y));
                    st.push((x, y));
                }
            }
        }
        false
    }
}
