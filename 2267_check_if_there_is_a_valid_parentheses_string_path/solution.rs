// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

use std::collections::HashSet;

impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        if (m + n - 1) % 2 == 1 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(' {
            return false;
        }
        let mut vis = HashSet::new();
        fn dfs(
            r: usize,
            c: usize,
            mut bal: i32,
            grid: &[Vec<char>],
            vis: &mut HashSet<(usize, usize, i32)>,
        ) -> bool {
            let m = grid.len();
            let n = grid[0].len();
            if r >= m || c >= n {
                return false;
            }
            bal += if grid[r][c] == '(' { 1 } else { -1 };
            if bal < 0 {
                return false;
            }
            if r == m - 1 && c == n - 1 {
                return bal == 0;
            }
            if !vis.insert((r, c, bal)) {
                return false;
            }
            dfs(r + 1, c, bal, grid, vis) || dfs(r, c + 1, bal, grid, vis)
        }
        dfs(0, 0, 0, &grid, &mut vis)
    }
}
