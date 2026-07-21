// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

impl Solution {
    pub fn largest_magic_square(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut row_prefix = vec![vec![0i32; cols + 1]; rows];
        let mut col_prefix = vec![vec![0i32; rows + 1]; cols];
        for i in 0..rows {
            for j in 0..cols {
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j];
                col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j];
            }
        }
        let row_sum = |row: usize, col_start: usize, col_end: usize| -> i32 {
            row_prefix[row][col_end + 1] - row_prefix[row][col_start]
        };
        let col_sum = |col: usize, row_start: usize, row_end: usize| -> i32 {
            col_prefix[col][row_end + 1] - col_prefix[col][row_start]
        };
        let is_magic = |row_start: usize, col_start: usize, size: usize| -> bool {
            let target = row_sum(row_start, col_start, col_start + size - 1);
            for row in row_start..row_start + size {
                if row_sum(row, col_start, col_start + size - 1) != target {
                    return false;
                }
            }
            for col in col_start..col_start + size {
                if col_sum(col, row_start, row_start + size - 1) != target {
                    return false;
                }
            }
            let mut diag1 = 0;
            let mut diag2 = 0;
            for offset in 0..size {
                diag1 += grid[row_start + offset][col_start + offset];
                diag2 += grid[row_start + offset][col_start + size - 1 - offset];
            }
            diag1 == target && diag2 == target
        };
        for size in (1..=rows.min(cols)).rev() {
            for row_start in 0..=rows - size {
                for col_start in 0..=cols - size {
                    if is_magic(row_start, col_start, size) {
                        return size as i32;
                    }
                }
            }
        }
        1
    }
}
