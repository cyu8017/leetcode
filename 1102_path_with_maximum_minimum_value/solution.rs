// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

use std::collections::BinaryHeap;

impl Solution {
    pub fn maximum_minimum_path(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut heap = BinaryHeap::new();
        heap.push((grid[0][0], 0usize, 0usize));
        let mut seen = vec![vec![false; n]; m];
        seen[0][0] = true;
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((val, r, c)) = heap.pop() {
            if r == m - 1 && c == n - 1 {
                return val;
            }
            for (dr, dc) in dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                    let nr = nr as usize;
                    let nc = nc as usize;
                    if !seen[nr][nc] {
                        seen[nr][nc] = true;
                        heap.push((val.min(grid[nr][nc]), nr, nc));
                    }
                }
            }
        }
        grid[0][0]
    }
}
