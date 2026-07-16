// LeetCode 0463 - Island Perimeter
// https://leetcode.com/problems/island-perimeter/

impl Solution {
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut perimeter = 0;
        for row in 0..rows {
            for col in 0..cols {
                if grid[row][col] == 0 {
                    continue;
                }
                perimeter += 4;
                if row > 0 && grid[row - 1][col] == 1 {
                    perimeter -= 2;
                }
                if col > 0 && grid[row][col - 1] == 1 {
                    perimeter -= 2;
                }
            }
        }
        perimeter
    }
}
