// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

impl Solution {
    pub fn closed_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut flood = |grid: &mut [Vec<i32>], sr: usize, sc: usize| -> bool {
            let mut stack = vec![(sr, sc)];
            grid[sr][sc] = 1;
            let mut closed = true;
            while let Some((r, c)) = stack.pop() {
                if r == 0 || r == m - 1 || c == 0 || c == n - 1 {
                    closed = false;
                }
                for (dr, dc) in [(1isize, 0), (-1, 0), (0, 1), (0, -1)] {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    if nr >= 0 && nr < m as isize && nc >= 0 && nc < n as isize {
                        let nr = nr as usize;
                        let nc = nc as usize;
                        if grid[nr][nc] == 0 {
                            grid[nr][nc] = 1;
                            stack.push((nr, nc));
                        }
                    }
                }
            }
            closed
        };
        let mut ans = 0;
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] == 0 && flood(&mut grid, r, c) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
