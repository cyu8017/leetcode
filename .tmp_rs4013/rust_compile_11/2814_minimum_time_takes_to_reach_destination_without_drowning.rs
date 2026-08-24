struct Solution;
fn main() {}

// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

use std::collections::VecDeque;

impl Solution {
    pub fn minimum_seconds(land: Vec<Vec<String>>) -> i32 {
        let m = land.len();
        let n = land[0].len();
        const INF: i32 = 1 << 30;
        let mut water = vec![vec![INF; n]; m];
        let mut wq = VecDeque::new();
        let mut start = (0, 0);
        let mut dest = (0, 0);
        for i in 0..m {
            for j in 0..n {
                if land[i][j] == "*" {
                    water[i][j] = 0;
                    wq.push_back((i, j));
                } else if land[i][j] == "S" {
                    start = (i, j);
                } else if land[i][j] == "D" {
                    dest = (i, j);
                }
            }
        }
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        while let Some((x, y)) = wq.pop_front() {
            for (dx, dy) in dirs {
                let ni = x as i32 + dx;
                let nj = y as i32 + dy;
                if ni < 0 || nj < 0 || ni >= m as i32 || nj >= n as i32 {
                    continue;
                }
                let (ni, nj) = (ni as usize, nj as usize);
                if land[ni][nj] == "X" || land[ni][nj] == "D" {
                    continue;
                }
                if water[ni][nj] > water[x][y] + 1 {
                    water[ni][nj] = water[x][y] + 1;
                    wq.push_back((ni, nj));
                }
            }
        }
        let mut dist = vec![vec![-1; n]; m];
        let mut q = VecDeque::new();
        q.push_back(start);
        dist[start.0][start.1] = 0;
        while let Some((x, y)) = q.pop_front() {
            if (x, y) == dest {
                return dist[x][y];
            }
            for (dx, dy) in dirs {
                let ni = x as i32 + dx;
                let nj = y as i32 + dy;
                if ni < 0 || nj < 0 || ni >= m as i32 || nj >= n as i32 {
                    continue;
                }
                let (ni, nj) = (ni as usize, nj as usize);
                if dist[ni][nj] != -1 || land[ni][nj] == "X" {
                    continue;
                }
                let nd = dist[x][y] + 1;
                if land[ni][nj] != "D" && nd >= water[ni][nj] {
                    continue;
                }
                dist[ni][nj] = nd;
                q.push_back((ni, nj));
            }
        }
        -1
    }
}
