// LeetCode 0407 - Trapping Rain Water II
// https://leetcode.com/problems/trapping-rain-water-ii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        if height_map.is_empty() || height_map[0].is_empty() {
            return 0;
        }

        let rows = height_map.len();
        let cols = height_map[0].len();
        if rows < 3 || cols < 3 {
            return 0;
        }

        let mut visited = vec![vec![false; cols]; rows];
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();

        for row in 0..rows {
            for col in 0..cols {
                if row == 0 || row == rows - 1 || col == 0 || col == cols - 1 {
                    heap.push(Reverse((height_map[row][col], row, col)));
                    visited[row][col] = true;
                }
            }
        }

        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        let mut trapped = 0;

        while let Some(Reverse((height, row, col))) = heap.pop() {
            for (delta_row, delta_col) in directions {
                let next_row = row as i32 + delta_row;
                let next_col = col as i32 + delta_col;
                if next_row < 0
                    || next_col < 0
                    || next_row as usize >= rows
                    || next_col as usize >= cols
                {
                    continue;
                }

                let next_row = next_row as usize;
                let next_col = next_col as usize;
                if visited[next_row][next_col] {
                    continue;
                }

                visited[next_row][next_col] = true;
                let next_height = height_map[next_row][next_col];
                trapped += (height - next_height).max(0);
                heap.push(Reverse((height.max(next_height), next_row, next_col)));
            }
        }

        trapped
    }
}
