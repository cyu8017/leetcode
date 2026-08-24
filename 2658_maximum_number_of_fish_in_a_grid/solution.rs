// LeetCode 2658 - Maximum Number of Fish in a Grid
// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

impl Solution {
    pub fn find_max_fish(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        fn dfs(grid: &mut [Vec<i32>], r: i32, c: i32, m: i32, n: i32) -> i32 {
            if r < 0 || r >= m || c < 0 || c >= n || grid[r as usize][c as usize] == 0 {
                return 0;
            }
            let fish = grid[r as usize][c as usize];
            grid[r as usize][c as usize] = 0;
            fish + dfs(grid, r + 1, c, m, n)
                + dfs(grid, r - 1, c, m, n)
                + dfs(grid, r, c + 1, m, n)
                + dfs(grid, r, c - 1, m, n)
        }
        let mut best = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] > 0 {
                    best = best.max(dfs(&mut grid, i as i32, j as i32, m as i32, n as i32));
                }
            }
        }
        best
    }
}
