// LeetCode 1162 - As Far from Land as Possible
// https://leetcode.com/problems/as-far-from-land-as-possible/

use std::collections::VecDeque;

impl Solution {
    pub fn max_distance(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut queue = VecDeque::new();
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 1 {
                    queue.push_back((i, j));
                }
            }
        }
        if queue.is_empty() || queue.len() == n * n {
            return -1;
        }
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        let mut dist = -1;
        while !queue.is_empty() {
            let size = queue.len();
            dist += 1;
            for _ in 0..size {
                let (r, c) = queue.pop_front().unwrap();
                for (dr, dc) in dirs {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    if nr >= 0 && nr < n as isize && nc >= 0 && nc < n as isize {
                        let nr = nr as usize;
                        let nc = nc as usize;
                        if grid[nr][nc] == 0 {
                            grid[nr][nc] = 1;
                            queue.push_back((nr, nc));
                        }
                    }
                }
            }
        }
        dist
    }
}
