// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let cells: Vec<Vec<u8>> = grid.iter().map(|row| row.bytes().collect()).collect();
        let mut all_keys = 0;
        let mut sr = 0;
        let mut sc = 0;
        for i in 0..m {
            for j in 0..n {
                let cell = cells[i][j];
                if cell == b'@' {
                    sr = i;
                    sc = j;
                } else if (b'a'..=b'f').contains(&cell) {
                    all_keys |= 1 << (cell - b'a');
                }
            }
        }
        let encode = |r: usize, c: usize, mask: i32| ((r as i64) << 20) | ((c as i64) << 10) | mask as i64;
        let mut queue = VecDeque::from([(sr, sc, 0i32, 0i32)]);
        let mut seen = HashSet::from([encode(sr, sc, 0)]);
        let dr = [1i32, -1, 0, 0];
        let dc = [0i32, 0, 1, -1];
        while let Some((r, c, mask, dist)) = queue.pop_front() {
            if mask == all_keys {
                return dist;
            }
            for k in 0..4 {
                let nr = r as i32 + dr[k];
                let nc = c as i32 + dc[k];
                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                let (nr, nc) = (nr as usize, nc as usize);
                let cell = cells[nr][nc];
                if cell == b'#' {
                    continue;
                }
                let mut nmask = mask;
                if (b'a'..=b'f').contains(&cell) {
                    nmask |= 1 << (cell - b'a');
                }
                if (b'A'..=b'F').contains(&cell) && mask & (1 << (cell - b'A')) == 0 {
                    continue;
                }
                let state = encode(nr, nc, nmask);
                if seen.insert(state) {
                    queue.push_back((nr, nc, nmask, dist + 1));
                }
            }
        }
        -1
    }
}
