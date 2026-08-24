// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn min_moves(matrix: Vec<String>) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        let grid: Vec<Vec<u8>> = matrix.iter().map(|s| s.as_bytes().to_vec()).collect();
        let mut g: HashMap<u8, Vec<(usize, usize)>> = HashMap::new();
        for i in 0..m {
            for j in 0..n {
                if grid[i][j].is_ascii_alphabetic() {
                    g.entry(grid[i][j]).or_default().push((i, j));
                }
            }
        }
        let dirs = [-1i32, 0, 1, 0, -1];
        const INF: i32 = 1 << 30;
        let mut dist = vec![vec![INF; n]; m];
        dist[0][0] = 0;
        let mut q = VecDeque::new();
        q.push_back((0usize, 0usize));
        while let Some((i, j)) = q.pop_front() {
            let d = dist[i][j];
            if i == m - 1 && j == n - 1 {
                return d;
            }
            let c = grid[i][j];
            if let Some(ports) = g.remove(&c) {
                for (x, y) in ports {
                    if d < dist[x][y] {
                        dist[x][y] = d;
                        q.push_front((x, y));
                    }
                }
            }
            for idx in 0..4 {
                let x = i as i32 + dirs[idx];
                let y = j as i32 + dirs[idx + 1];
                if x >= 0 && x < m as i32 && y >= 0 && y < n as i32 {
                    let (x, y) = (x as usize, y as usize);
                    if grid[x][y] != b'#' && d + 1 < dist[x][y] {
                        dist[x][y] = d + 1;
                        q.push_back((x, y));
                    }
                }
            }
        }
        -1
    }
}
