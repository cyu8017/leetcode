// LeetCode 0778 - Swim in Rising Water
// https://leetcode.com/problems/swim-in-rising-water/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut heap = BinaryHeap::new();
        let mut seen = vec![vec![false; n]; n];
        heap.push(Reverse((grid[0][0], 0usize, 0usize)));
        seen[0][0] = true;
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        while let Some(Reverse((time, r, c))) = heap.pop() {
            if r == n - 1 && c == n - 1 {
                return time;
            }
            for (dr, dc) in dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < n as i32 && nc >= 0 && nc < n as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if !seen[nr][nc] {
                        seen[nr][nc] = true;
                        heap.push(Reverse((time.max(grid[nr][nc]), nr, nc)));
                    }
                }
            }
        }
        -1
    }
}
