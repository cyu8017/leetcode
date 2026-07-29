// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

use std::collections::VecDeque;

impl Solution {
    pub fn shortest_path_binary_matrix(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        if grid[0][0] != 0 || grid[n - 1][n - 1] != 0 {
            return -1;
        }
        let mut queue = VecDeque::new();
        queue.push_back((0usize, 0usize, 1i32));
        grid[0][0] = 1;
        while let Some((r, c, dist)) = queue.pop_front() {
            if r == n - 1 && c == n - 1 {
                return dist;
            }
            for dr in [-1i32, 0, 1] {
                for dc in [-1i32, 0, 1] {
                    if dr == 0 && dc == 0 {
                        continue;
                    }
                    let nr = r as i32 + dr;
                    let nc = c as i32 + dc;
                    if nr >= 0
                        && nc >= 0
                        && (nr as usize) < n
                        && (nc as usize) < n
                        && grid[nr as usize][nc as usize] == 0
                    {
                        grid[nr as usize][nc as usize] = 1;
                        queue.push_back((nr as usize, nc as usize, dist + 1));
                    }
                }
            }
        }
        -1
    }
}
