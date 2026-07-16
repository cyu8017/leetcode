// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

use std::collections::VecDeque;

impl Solution {
    pub fn walls_and_gates(rooms: &mut Vec<Vec<i32>>) {
        if rooms.is_empty() || rooms[0].is_empty() {
            return;
        }

        let rows = rooms.len();
        let cols = rooms[0].len();
        let mut queue = VecDeque::new();

        for row in 0..rows {
            for col in 0..cols {
                if rooms[row][col] == 0 {
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
                    if rooms[next_row][next_col] == i32::MAX {
                        rooms[next_row][next_col] = rooms[row][col] + 1;
                        queue.push_back((next_row, next_col));
                    }
                }
            }
        }
    }
}
