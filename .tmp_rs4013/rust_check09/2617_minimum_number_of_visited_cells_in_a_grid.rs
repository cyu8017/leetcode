struct Solution;

// LeetCode 2617 - Minimum Number of Visited Cells in a Grid
// https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_visited_cells(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![-1; n]; m];
        let mut q = VecDeque::new();
        q.push_back((0usize, 0usize));
        dist[0][0] = 1;
        while let Some((r, c)) = q.pop_front() {
            if r == m - 1 && c == n - 1 {
                return dist[r][c];
            }
            let max_c = (c + grid[r][c] as usize).min(n - 1);
            for nc in c + 1..=max_c {
                if dist[r][nc] == -1 {
                    dist[r][nc] = dist[r][c] + 1;
                    q.push_back((r, nc));
                }
            }
            let max_r = (r + grid[r][c] as usize).min(m - 1);
            for nr in r + 1..=max_r {
                if dist[nr][c] == -1 {
                    dist[nr][c] = dist[r][c] + 1;
                    q.push_back((nr, c));
                }
            }
        }
        -1
    }
}

fn main() {}
