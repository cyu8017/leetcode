// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let m = move_time.len();
        let n = move_time[0].len();
        const INF: i32 = 1 << 30;
        let mut dist = vec![vec![[INF; 2]; n]; m];
        let mut pq = BinaryHeap::new();
        dist[0][0][0] = 0;
        pq.push(Reverse((0, 0usize, 0usize, 0usize)));
        const DIRS: [[i32; 2]; 4] = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        while let Some(Reverse((t, r, c, parity))) = pq.pop() {
            if t != dist[r][c][parity] {
                continue;
            }
            if r == m - 1 && c == n - 1 {
                return t;
            }
            let cost = if parity == 1 { 2 } else { 1 };
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
                let nt = start + cost;
                let np = 1 - parity;
                if nt < dist[nr][nc][np] {
                    dist[nr][nc][np] = nt;
                    pq.push(Reverse((nt, nr, nc, np)));
                }
            }
        }
        -1
    }
}
