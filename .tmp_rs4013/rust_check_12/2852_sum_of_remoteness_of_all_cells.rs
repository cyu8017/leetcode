struct Solution;
// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

use std::collections::VecDeque;

impl Solution {
    pub fn sum_remoteness(grid: Vec<Vec<i32>>) -> i64 {
        let m = grid.len();
        let n = grid[0].len();
        let mut seen = vec![vec![false; n]; m];
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        let mut total = 0i64;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != -1 {
                    total += grid[i][j] as i64;
                }
            }
        }
        let mut ans = 0i64;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == -1 || seen[i][j] {
                    continue;
                }
                let mut q = VecDeque::new();
                q.push_back((i, j));
                seen[i][j] = true;
                let mut sum = 0i64;
                let mut cnt = 0i64;
                while let Some((x, y)) = q.pop_front() {
                    sum += grid[x][y] as i64;
                    cnt += 1;
                    for (dx, dy) in dirs {
                        let ni = x as i32 + dx;
                        let nj = y as i32 + dy;
                        if ni >= 0
                            && nj >= 0
                            && (ni as usize) < m
                            && (nj as usize) < n
                            && !seen[ni as usize][nj as usize]
                            && grid[ni as usize][nj as usize] != -1
                        {
                            seen[ni as usize][nj as usize] = true;
                            q.push_back((ni as usize, nj as usize));
                        }
                    }
                }
                ans += (total - sum) * cnt;
            }
        }
        ans
    }
}

fn main() {}
