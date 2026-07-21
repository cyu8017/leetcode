// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_shortest_path(
        grid: Vec<Vec<i32>>,
        r1: i32,
        c1: i32,
        r2: i32,
        c2: i32,
    ) -> i32 {
        if r1 == r2 && c1 == c2 {
            return 0;
        }
        let m = grid.len();
        let n = grid[0].len();
        let dirs = [(-1i32, 0i32), (1, 0), (0, -1), (0, 1)];
        let mut dist = vec![vec![i32::MAX; n]; m];
        let mut heap = BinaryHeap::new();
        let (sr, sc) = (r1 as usize, c1 as usize);
        dist[sr][sc] = 0;
        heap.push(Reverse((0i32, r1, c1)));

        while let Some(Reverse((d, r, c))) = heap.pop() {
            if r == r2 && c == c2 {
                return d;
            }
            if d > dist[r as usize][c as usize] {
                continue;
            }
            for &(dr, dc) in &dirs {
                let nr = r + dr;
                let nc = c + dc;
                if nr < 0 || nr >= m as i32 || nc < 0 || nc >= n as i32 {
                    continue;
                }
                let (nr_u, nc_u) = (nr as usize, nc as usize);
                if grid[nr_u][nc_u] == 0 {
                    continue;
                }
                let nd = d + grid[nr_u][nc_u];
                if nd < dist[nr_u][nc_u] {
                    dist[nr_u][nc_u] = nd;
                    heap.push(Reverse((nd, nr, nc)));
                }
            }
        }
        -1
    }
}
