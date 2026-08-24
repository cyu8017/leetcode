// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_minutes(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        const INF: i32 = 1_000_000_000;
        let mut fire = vec![vec![INF; n]; m];
        let mut q = VecDeque::new();
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    fire[i][j] = 0;
                    q.push_back((i, j));
                }
            }
        }
        let dirs = [(1isize, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c)) = q.pop_front() {
            for &(dr, dc) in &dirs {
                let nr = r as isize + dr;
                let nc = c as isize + dc;
                if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                if grid[nr][nc] == 2 || fire[nr][nc] != INF {
                    continue;
                }
                fire[nr][nc] = fire[r][c] + 1;
                q.push_back((nr, nc));
            }
        }
        let can = |wait: i32| -> bool {
            if wait >= fire[0][0] {
                return false;
            }
            let mut vis = vec![vec![false; n]; m];
            let mut qq = VecDeque::new();
            qq.push_back((0usize, 0usize, wait));
            vis[0][0] = true;
            while let Some((r, c, t)) = qq.pop_front() {
                for &(dr, dc) in &dirs {
                    let nr = r as isize + dr;
                    let nc = c as isize + dc;
                    let nt = t + 1;
                    if nr < 0 || nr >= m as isize || nc < 0 || nc >= n as isize {
                        continue;
                    }
                    let (nr, nc) = (nr as usize, nc as usize);
                    if grid[nr][nc] == 2 || vis[nr][nc] {
                        continue;
                    }
                    if nr == m - 1 && nc == n - 1 {
                        if nt <= fire[nr][nc] {
                            return true;
                        }
                        continue;
                    }
                    if nt >= fire[nr][nc] {
                        continue;
                    }
                    vis[nr][nc] = true;
                    qq.push_back((nr, nc, nt));
                }
            }
            false
        };
        let mut lo = 0;
        let mut hi = (m * n + 10) as i32;
        let mut ans = -1;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if can(mid) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        if ans >= (m * n) as i32 {
            INF
        } else {
            ans
        }
    }
}
