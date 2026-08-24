struct Solution;
// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let m = move_time.len();
        let n = move_time[0].len();
        let mut dist = vec![vec![1 << 30; n]; m];
        let mut h = BinaryHeap::new();
        h.push(Reverse((0, 0usize, 0usize)));
        dist[0][0] = 0;
        const DIRS: [[i32; 2]; 4] = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        while let Some(Reverse((t, r, c))) = h.pop() {
            if t != dist[r][c] {
                continue;
            }
            if r == m - 1 && c == n - 1 {
                return t;
            }
            for d in &DIRS {
                let nr = r as i32 + d[0];
                let nc = c as i32 + d[1];
                if nr < 0 || nc < 0 || nr >= m as i32 || nc >= n as i32 {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                let mut start = t;
                if move_time[nr][nc] > start {
                    start = move_time[nr][nc];
                }
                let nt = start + 1;
                if nt < dist[nr][nc] {
                    dist[nr][nc] = nt;
                    h.push(Reverse((nt, nr, nc)));
                }
            }
        }
        -1
    }
}

fn main() {}
