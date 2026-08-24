// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        if rows < 3 || cols < 3 {
            return 0;
        }
        let mut ans = 0;
        for i in 0..rows - 2 {
            for j in 0..cols - 2 {
                if Self::magic(&grid, i, j) {
                    ans += 1;
                }
            }
        }
        ans
    }

    fn magic(grid: &[Vec<i32>], r: usize, c: usize) -> bool {
        let mut vals = Vec::new();
        for i in 0..3 {
            for j in 0..3 {
                vals.push(grid[r + i][c + j]);
            }
        }
        vals.sort_unstable();
        for i in 0..9 {
            if vals[i] != i as i32 + 1 {
                return false;
            }
        }
        grid[r][c] + grid[r][c + 1] + grid[r][c + 2] == 15
            && grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] == 15
            && grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] == 15
            && grid[r][c] + grid[r + 1][c] + grid[r + 2][c] == 15
            && grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] == 15
            && grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] == 15
            && grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] == 15
            && grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] == 15
    }
}
