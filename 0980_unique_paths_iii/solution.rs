// LeetCode 0980 - Unique Paths III
// https://leetcode.com/problems/unique-paths-iii/

impl Solution {
    pub fn unique_paths_iii(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut empty = 0;
        let mut sr = 0;
        let mut sc = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != -1 {
                    empty += 1;
                }
                if grid[i][j] == 1 {
                    sr = i;
                    sc = j;
                }
            }
        }
        fn dfs(grid: &mut Vec<Vec<i32>>, r: usize, c: usize, remain: i32, ans: &mut i32) {
            if grid[r][c] == 2 {
                if remain == 1 {
                    *ans += 1;
                }
                return;
            }
            let temp = grid[r][c];
            grid[r][c] = -1;
            let m = grid.len() as i32;
            let n = grid[0].len() as i32;
            let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
            for (dr, dc) in dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr as usize][nc as usize] != -1 {
                    dfs(grid, nr as usize, nc as usize, remain - 1, ans);
                }
            }
            grid[r][c] = temp;
        }
        let mut ans = 0;
        dfs(&mut grid, sr, sc, empty, &mut ans);
        ans
    }
}
