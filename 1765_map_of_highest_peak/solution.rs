// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

use std::collections::VecDeque;

impl Solution {
    pub fn highest_peak(is_water: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = is_water.len();
        let n = is_water[0].len();
        let mut dist = vec![vec![-1i32; n]; m];
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        for i in 0..m {
            for j in 0..n {
                if is_water[i][j] == 1 {
                    dist[i][j] = 0;
                    queue.push_back((i, j));
                }
            }
        }
        let dirs: [(i32, i32); 4] = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some((i, j)) = queue.pop_front() {
            for &(di, dj) in dirs.iter() {
                let x = i as i32 + di;
                let y = j as i32 + dj;
                if x >= 0 && x < m as i32 && y >= 0 && y < n as i32 {
                    let (x, y) = (x as usize, y as usize);
                    if dist[x][y] == -1 {
                        dist[x][y] = dist[i][j] + 1;
                        queue.push_back((x, y));
                    }
                }
            }
        }
        dist
    }
}
