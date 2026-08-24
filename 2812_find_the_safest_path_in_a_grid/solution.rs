// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_safeness_factor(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut dist = vec![vec![-1; n]; n];
        let mut q = VecDeque::new();
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 1 {
                    dist[i][j] = 0;
                    q.push_back((i, j));
                }
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((x, y)) = q.pop_front() {
            for (dx, dy) in dirs {
                let ni = x as i32 + dx;
                let nj = y as i32 + dy;
                if ni >= 0 && nj >= 0 && ni < n as i32 && nj < n as i32 {
                    let (ni, nj) = (ni as usize, nj as usize);
                    if dist[ni][nj] == -1 {
                        dist[ni][nj] = dist[x][y] + 1;
                        q.push_back((ni, nj));
                    }
                }
            }
        }
        let ok = |sf: i32| {
            if dist[0][0] < sf {
                return false;
            }
            let mut seen = vec![vec![false; n]; n];
            let mut st = vec![(0usize, 0usize)];
            seen[0][0] = true;
            while let Some((x, y)) = st.pop() {
                if x == n - 1 && y == n - 1 {
                    return true;
                }
                for (dx, dy) in dirs {
                    let ni = x as i32 + dx;
                    let nj = y as i32 + dy;
                    if ni >= 0 && nj >= 0 && ni < n as i32 && nj < n as i32 {
                        let (ni, nj) = (ni as usize, nj as usize);
                        if !seen[ni][nj] && dist[ni][nj] >= sf {
                            seen[ni][nj] = true;
                            st.push((ni, nj));
                        }
                    }
                }
            }
            false
        };
        let mut lo = 0;
        let mut hi = (n * n) as i32;
        let mut ans = 0;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if ok(mid) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        ans
    }
}
