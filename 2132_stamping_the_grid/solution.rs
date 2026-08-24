// LeetCode 2132 - Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/

impl Solution {
    pub fn possible_to_stamp(grid: Vec<Vec<i32>>, stamp_height: i32, stamp_width: i32) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let sh = stamp_height as usize;
        let sw = stamp_width as usize;
        let mut pref = vec![vec![0i32; n + 1]; m + 1];
        for i in 0..m {
            for j in 0..n {
                pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j];
            }
        }
        let sum = |r1: usize, c1: usize, r2: usize, c2: usize| {
            pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]
        };
        let mut diff = vec![vec![0i32; n + 1]; m + 1];
        if m >= sh && n >= sw {
            for i in 0..=m - sh {
                for j in 0..=n - sw {
                    if sum(i, j, i + sh - 1, j + sw - 1) == 0 {
                        diff[i][j] += 1;
                        diff[i][j + sw] -= 1;
                        diff[i + sh][j] -= 1;
                        diff[i + sh][j + sw] += 1;
                    }
                }
            }
        }
        let mut cur = vec![vec![0i32; n]; m];
        for i in 0..m {
            for j in 0..n {
                let mut v = diff[i][j];
                if i > 0 {
                    v += cur[i - 1][j];
                }
                if j > 0 {
                    v += cur[i][j - 1];
                }
                if i > 0 && j > 0 {
                    v -= cur[i - 1][j - 1];
                }
                cur[i][j] = v;
                if grid[i][j] == 0 && v == 0 {
                    return false;
                }
            }
        }
        true
    }
}
