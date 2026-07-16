// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

use std::collections::VecDeque;

impl Solution {
    pub fn update_matrix(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = mat.len();
        let cols = mat[0].len();
        const INF: i32 = 1_000_000_000;
        let mut dist = vec![vec![INF; cols]; rows];
        let mut queue = VecDeque::new();

        for row in 0..rows {
            for col in 0..cols {
                if mat[row][col] == 0 {
                    dist[row][col] = 0;
                    queue.push_back((row, col));
                }
            }
        }

        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((row, col)) = queue.pop_front() {
            for (dr, dc) in directions {
                let next_row = row as i32 + dr;
                let next_col = col as i32 + dc;
                if next_row >= 0
                    && next_row < rows as i32
                    && next_col >= 0
                    && next_col < cols as i32
                {
                    let next_row = next_row as usize;
                    let next_col = next_col as usize;
                    if dist[next_row][next_col] > dist[row][col] + 1 {
                        dist[next_row][next_col] = dist[row][col] + 1;
                        queue.push_back((next_row, next_col));
                    }
                }
            }
        }

        dist
    }
}
