// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

impl Solution {
    pub fn minimum_sum(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len() as i32;
        let n = grid[0].len() as i32;
        let mut ans = m * n;
        const INF: i32 = i32::MAX / 4;
        let f = |i1: i32, j1: i32, i2: i32, j2: i32| -> i32 {
            let mut x1 = INF;
            let mut y1 = INF;
            let mut x2 = -INF;
            let mut y2 = -INF;
            for i in i1..=i2 {
                for j in j1..=j2 {
                    if grid[i as usize][j as usize] == 1 {
                        x1 = x1.min(i);
                        y1 = y1.min(j);
                        x2 = x2.max(i);
                        y2 = y2.max(j);
                    }
                }
            }
            if x1 == INF {
                0
            } else {
                (x2 - x1 + 1) * (y2 - y1 + 1)
            }
        };
        for i1 in 0..m - 1 {
            for i2 in i1 + 1..m - 1 {
                ans = ans.min(f(0, 0, i1, n - 1) + f(i1 + 1, 0, i2, n - 1) + f(i2 + 1, 0, m - 1, n - 1));
            }
        }
        for j1 in 0..n - 1 {
            for j2 in j1 + 1..n - 1 {
                ans = ans.min(f(0, 0, m - 1, j1) + f(0, j1 + 1, m - 1, j2) + f(0, j2 + 1, m - 1, n - 1));
            }
        }
        for i in 0..m - 1 {
            for j in 0..n - 1 {
                ans = ans.min(f(0, 0, i, j) + f(0, j + 1, i, n - 1) + f(i + 1, 0, m - 1, n - 1));
                ans = ans.min(f(0, 0, i, n - 1) + f(i + 1, 0, m - 1, j) + f(i + 1, j + 1, m - 1, n - 1));
                ans = ans.min(f(0, 0, i, j) + f(i + 1, 0, m - 1, j) + f(0, j + 1, m - 1, n - 1));
                ans = ans.min(f(0, 0, m - 1, j) + f(0, j + 1, i, n - 1) + f(i + 1, j + 1, m - 1, n - 1));
            }
        }
        ans
    }
}
