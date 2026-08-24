// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

impl Solution {
    pub fn count_unguarded(m: i32, n: i32, guards: Vec<Vec<i32>>, walls: Vec<Vec<i32>>) -> i32 {
        let m = m as usize;
        let n = n as usize;
        let mut grid = vec![vec![0i32; n]; m];
        for w in &walls {
            grid[w[0] as usize][w[1] as usize] = 2;
        }
        for g in &guards {
            grid[g[0] as usize][g[1] as usize] = 2;
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        for g in &guards {
            for &(dr, dc) in &dirs {
                let mut r = g[0] + dr;
                let mut c = g[1] + dc;
                while r >= 0 && r < m as i32 && c >= 0 && c < n as i32 && grid[r as usize][c as usize] != 2 {
                    grid[r as usize][c as usize] = 1;
                    r += dr;
                    c += dc;
                }
            }
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
