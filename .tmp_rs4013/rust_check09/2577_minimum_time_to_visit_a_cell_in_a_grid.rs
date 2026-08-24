struct Solution;

// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_time(grid: Vec<Vec<i32>>) -> i32 {
        if grid[0][1] > 1 && grid[1][0] > 1 {
            return -1;
        }
        let m = grid.len();
        let n = grid[0].len();
        let mut dist = vec![vec![i32::MAX / 2; n]; m];
        let mut h = BinaryHeap::new();
        h.push(Reverse((0, 0usize, 0usize)));
        dist[0][0] = 0;
        let dirs = [(1isize, 0isize), (-1, 0), (0, 1), (0, -1)];
        while let Some(Reverse((t, r, c))) = h.pop() {
            if r == m - 1 && c == n - 1 {
                return t;
            }
            if t > dist[r][c] {
                continue;
            }
            for (dr, dc) in dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let nr = nr as usize;
                let nc = nc as usize;
                let mut nt = t + 1;
                if nt < grid[nr][nc] {
                    let mut wait = grid[nr][nc] - nt;
                    if wait % 2 == 1 {
                        wait += 1;
                    }
                    nt += wait;
                }
                if nt < dist[nr][nc] {
                    dist[nr][nc] = nt;
                    h.push(Reverse((nt, nr, nc)));
                }
            }
        }
        -1
    }
}

fn main() {}
