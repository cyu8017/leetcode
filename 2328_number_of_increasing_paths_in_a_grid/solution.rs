// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

impl Solution {
    pub fn count_paths(grid: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![vec![0i32; n]; m];
        let dirs = [(1isize, 0isize), (-1, 0), (0, 1), (0, -1)];
        fn dfs(
            r: usize,
            c: usize,
            grid: &[Vec<i32>],
            dp: &mut [Vec<i32>],
            dirs: &[(isize, isize)],
        ) -> i32 {
            if dp[r][c] != 0 {
                return dp[r][c];
            }
            let mut res = 1;
            for &(dr, dc) in dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr >= 0
                    && nr < grid.len() as isize
                    && nc >= 0
                    && nc < grid[0].len() as isize
                    && grid[nr as usize][nc as usize] > grid[r][c]
                {
                    res = (res + dfs(nr as usize, nc as usize, grid, dp, dirs)) % 1_000_000_007;
                }
            }
            dp[r][c] = res;
            res
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                ans = (ans + dfs(i, j, &grid, &mut dp, &dirs)) % MOD;
            }
        }
        ans
    }
}
