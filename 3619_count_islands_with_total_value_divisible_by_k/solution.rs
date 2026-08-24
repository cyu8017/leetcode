// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

impl Solution {
    pub fn count_islands(mut grid: Vec<Vec<i32>>, k: i32) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let dirs = [-1, 0, 1, 0, -1];
        fn dfs(grid: &mut [Vec<i32>], i: usize, j: usize, m: usize, n: usize, dirs: &[i32; 5]) -> i64 {
            let mut s = grid[i][j] as i64;
            grid[i][j] = 0;
            for d in 0..4 {
                let x = i as i32 + dirs[d];
                let y = j as i32 + dirs[d + 1];
                if x >= 0 && x < m as i32 && y >= 0 && y < n as i32 && grid[x as usize][y as usize] > 0 {
                    s += dfs(grid, x as usize, y as usize, m, n, dirs);
                }
            }
            s
        }
        let mut ans = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] > 0 && dfs(&mut grid, i, j, m, n, &dirs) % k as i64 == 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
