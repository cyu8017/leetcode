// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

use std::collections::VecDeque;

impl Solution {
    pub fn oranges_rotting(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut q = VecDeque::new();
        let mut fresh = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 2 {
                    q.push_back((i, j));
                } else if grid[i][j] == 1 {
                    fresh += 1;
                }
            }
        }
        let mut minutes = 0;
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        while !q.is_empty() && fresh > 0 {
            let sz = q.len();
            for _ in 0..sz {
                let (r, c) = q.pop_front().unwrap();
                for (dr, dc) in dirs {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    if nr >= 0
                        && nr < m as isize
                        && nc >= 0
                        && nc < n as isize
                        && grid[nr as usize][nc as usize] == 1
                    {
                        grid[nr as usize][nc as usize] = 2;
                        fresh -= 1;
                        q.push_back((nr as usize, nc as usize));
                    }
                }
            }
            minutes += 1;
        }
        if fresh == 0 { minutes } else { -1 }
    }
}
