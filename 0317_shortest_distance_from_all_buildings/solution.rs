// LeetCode 0317 - Shortest Distance from All Buildings
// https://leetcode.com/problems/shortest-distance-from-all-buildings/

use std::collections::VecDeque;

impl Solution {
    pub fn shortest_distance(grid: Vec<Vec<i32>>) -> i32 {
        if grid.is_empty() {
            return -1;
        }

        let rows = grid.len();
        let cols = grid[0].len();
        let buildings = grid
            .iter()
            .flat_map(|row| row.iter())
            .filter(|&&cell| cell == 1)
            .count();
        let mut distances = vec![vec![0; cols]; rows];
        let mut reach = vec![vec![0; cols]; rows];
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];

        for row in 0..rows {
            for col in 0..cols {
                if grid[row][col] != 1 {
                    continue;
                }
                let mut visited = vec![vec![false; cols]; rows];
                let mut queue = VecDeque::new();
                queue.push_back((row, col, 0));
                visited[row][col] = true;
                while let Some((current_row, current_col, distance)) = queue.pop_front() {
                    for (dr, dc) in directions {
                        let next_row = current_row as i32 + dr;
                        let next_col = current_col as i32 + dc;
                        if next_row >= 0
                            && next_row < rows as i32
                            && next_col >= 0
                            && next_col < cols as i32
                        {
                            let next_row = next_row as usize;
                            let next_col = next_col as usize;
                            if grid[next_row][next_col] == 0 && !visited[next_row][next_col] {
                                visited[next_row][next_col] = true;
                                distances[next_row][next_col] += distance + 1;
                                reach[next_row][next_col] += 1;
                                queue.push_back((next_row, next_col, distance + 1));
                            }
                        }
                    }
                }
            }
        }

        let mut best = i32::MAX;
        for row in 0..rows {
            for col in 0..cols {
                if grid[row][col] == 0 && reach[row][col] == buildings {
                    best = best.min(distances[row][col]);
                }
            }
        }

        if best == i32::MAX { -1 } else { best }
    }
}
