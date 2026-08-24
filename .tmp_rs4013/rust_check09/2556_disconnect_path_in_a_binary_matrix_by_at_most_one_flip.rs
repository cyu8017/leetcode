struct Solution;

// LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
// https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

impl Solution {
    pub fn is_possible_to_cut_path(mut grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        fn dfs(r: usize, c: usize, grid: &mut [Vec<i32>], m: usize, n: usize) -> bool {
            if r == m - 1 && c == n - 1 {
                return true;
            }
            if r >= m || c >= n || grid[r][c] == 0 {
                return false;
            }
            if !(r == 0 && c == 0) {
                grid[r][c] = 0;
            }
            dfs(r + 1, c, grid, m, n) || dfs(r, c + 1, grid, m, n)
        }
        if !dfs(0, 0, &mut grid, m, n) {
            return true;
        }
        grid[0][0] = 1;
        !dfs(0, 0, &mut grid, m, n)
    }
}

fn main() {}
