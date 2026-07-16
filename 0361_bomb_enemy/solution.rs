// LeetCode 0361 - Bomb Enemy
// https://leetcode.com/problems/bomb-enemy/

impl Solution {
    pub fn max_killed_enemies(grid: Vec<Vec<char>>) -> i32 {
        if grid.is_empty() || grid[0].is_empty() {
            return 0;
        }

        let rows = grid.len();
        let cols = grid[0].len();
        let mut row_hits = vec![vec![0; cols]; rows];
        let mut col_hits = vec![vec![0; cols]; rows];

        for row in 0..rows {
            let mut count = 0;
            for col in 0..cols {
                match grid[row][col] {
                    'W' => count = 0,
                    'E' => count += 1,
                    _ => row_hits[row][col] = count,
                }
            }
            count = 0;
            for col in (0..cols).rev() {
                match grid[row][col] {
                    'W' => count = 0,
                    'E' => count += 1,
                    _ => row_hits[row][col] += count,
                }
            }
        }

        for col in 0..cols {
            let mut count = 0;
            for row in 0..rows {
                match grid[row][col] {
                    'W' => count = 0,
                    'E' => count += 1,
                    _ => col_hits[row][col] = count,
                }
            }
            count = 0;
            for row in (0..rows).rev() {
                match grid[row][col] {
                    'W' => count = 0,
                    'E' => count += 1,
                    _ => col_hits[row][col] += count,
                }
            }
        }

        let mut result = 0;
        for row in 0..rows {
            for col in 0..cols {
                result = result.max(row_hits[row][col] + col_hits[row][col]);
            }
        }

        result
    }
}
