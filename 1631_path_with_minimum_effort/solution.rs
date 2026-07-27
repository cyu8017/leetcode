// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_effort_path(heights: Vec<Vec<i32>>) -> i32 {
        let m = heights.len();
        let n = heights[0].len();
        let mut dist = vec![vec![i32::MAX; n]; m];
        dist[0][0] = 0;
        let mut heap = BinaryHeap::new();
        heap.push(Reverse((0, 0usize, 0usize)));
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        while let Some(Reverse((effort, i, j))) = heap.pop() {
            if i == m - 1 && j == n - 1 {
                return effort;
            }
            if effort != dist[i][j] {
                continue;
            }
            for (di, dj) in dirs {
                let x = i as i32 + di;
                let y = j as i32 + dj;
                if x >= 0 && x < m as i32 && y >= 0 && y < n as i32 {
                    let (x, y) = (x as usize, y as usize);
                    let diff = (heights[i][j] - heights[x][y]).abs();
                    let nd = effort.max(diff);
                    if nd < dist[x][y] {
                        dist[x][y] = nd;
                        heap.push(Reverse((nd, x, y)));
                    }
                }
            }
        }
        0
    }
}
