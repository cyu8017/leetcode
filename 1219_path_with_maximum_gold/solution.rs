// LeetCode 1219 - Path with Maximum Gold
// https://leetcode.com/problems/path-with-maximum-gold/

impl Solution {
    pub fn get_maximum_gold(mut grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        fn dfs(grid: &mut [Vec<i32>], r: usize, c: usize, rows: usize, cols: usize) -> i32 {
            let gold = grid[r][c];
            grid[r][c] = 0;
            let mut best = 0;
            for (dr, dc) in [(1isize, 0), (-1, 0), (0, 1), (0, -1)] {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr >= 0 && nr < rows as isize && nc >= 0 && nc < cols as isize {
                    let nr = nr as usize;
                    let nc = nc as usize;
                    if grid[nr][nc] > 0 {
                        best = best.max(dfs(grid, nr, nc, rows, cols));
                    }
                }
            }
            grid[r][c] = gold;
            gold + best
        }
        let mut ans = 0;
        for r in 0..rows {
            for c in 0..cols {
                if grid[r][c] > 0 {
                    ans = ans.max(dfs(&mut grid, r, c, rows, cols));
                }
            }
        }
        ans
    }
}
