// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

impl Solution {
    pub fn num_enclaves(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        fn dfs(grid: &mut Vec<Vec<i32>>, r: isize, c: isize) {
            let m = grid.len() as isize;
            let n = grid[0].len() as isize;
            if r < 0 || r >= m || c < 0 || c >= n || grid[r as usize][c as usize] != 1 {
                return;
            }
            grid[r as usize][c as usize] = 0;
            dfs(grid, r + 1, c);
            dfs(grid, r - 1, c);
            dfs(grid, r, c + 1);
            dfs(grid, r, c - 1);
        }
        for i in 0..m {
            dfs(&mut grid, i as isize, 0);
            dfs(&mut grid, i as isize, (n - 1) as isize);
        }
        for j in 0..n {
            dfs(&mut grid, 0, j as isize);
            dfs(&mut grid, (m - 1) as isize, j as isize);
        }
        grid.iter().map(|row| row.iter().sum::<i32>()).sum()
    }
}
