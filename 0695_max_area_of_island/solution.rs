// LeetCode 0695 - Max Area of Island
// https://leetcode.com/problems/max-area-of-island/

impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut best = 0;
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                best = best.max(Self::dfs(&mut grid, i as i32, j as i32));
            }
        }
        best
    }

    fn dfs(grid: &mut [Vec<i32>], r: i32, c: i32) -> i32 {
        if r < 0
            || r >= grid.len() as i32
            || c < 0
            || c >= grid[0].len() as i32
            || grid[r as usize][c as usize] == 0
        {
            return 0;
        }
        grid[r as usize][c as usize] = 0;
        1 + Self::dfs(grid, r + 1, c)
            + Self::dfs(grid, r - 1, c)
            + Self::dfs(grid, r, c + 1)
            + Self::dfs(grid, r, c - 1)
    }
}
