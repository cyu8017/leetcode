// LeetCode 0200 - Number of Islands
// https://leetcode.com/problems/number-of-islands/

impl Solution {
    fn flood(grid: &mut Vec<Vec<char>>, row: isize, col: isize) {
        if row < 0 || col < 0 || row as usize >= grid.len() ||
            col as usize >= grid[row as usize].len() || grid[row as usize][col as usize] != '1' {
            return;
        }
        grid[row as usize][col as usize] = '0';
        Self::flood(grid, row + 1, col);
        Self::flood(grid, row - 1, col);
        Self::flood(grid, row, col + 1);
        Self::flood(grid, row, col - 1);
    }

    pub fn num_islands(grid: &mut Vec<Vec<char>>) -> i32 {
        if grid.is_empty() || grid[0].is_empty() {
            return 0;
        }

        let mut islands = 0;
        for row in 0..grid.len() {
            for col in 0..grid[row].len() {
                if grid[row][col] == '1' {
                    islands += 1;
                    Self::flood(grid, row as isize, col as isize);
                }
            }
        }
        islands
    }
}
