// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

use std::collections::HashSet;

impl Solution {
    pub fn has_path(maze: Vec<Vec<i32>>, start: Vec<i32>, destination: Vec<i32>) -> bool {
        let rows = maze.len() as i32;
        let cols = maze[0].len() as i32;
        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        let mut visited = HashSet::new();
        let mut stack = vec![(start[0], start[1])];

        while let Some((row, col)) = stack.pop() {
            if !visited.insert((row, col)) {
                continue;
            }
            if row == destination[0] && col == destination[1] {
                return true;
            }
            for (dr, dc) in directions {
                let mut next_row = row;
                let mut next_col = col;
                while next_row + dr >= 0
                    && next_row + dr < rows
                    && next_col + dc >= 0
                    && next_col + dc < cols
                    && maze[(next_row + dr) as usize][(next_col + dc) as usize] == 0
                {
                    next_row += dr;
                    next_col += dc;
                }
                if !visited.contains(&(next_row, next_col)) {
                    stack.push((next_row, next_col));
                }
            }
        }
        false
    }
}
