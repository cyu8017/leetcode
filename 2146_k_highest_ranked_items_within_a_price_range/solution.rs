// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

use std::collections::VecDeque;

impl Solution {
    pub fn highest_ranked_k_items(
        grid: Vec<Vec<i32>>,
        pricing: Vec<i32>,
        start: Vec<i32>,
        k: i32,
    ) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let (low, high) = (pricing[0], pricing[1]);
        let mut vis = vec![vec![false; n]; m];
        let mut q = VecDeque::new();
        q.push_back((start[0] as usize, start[1] as usize, 0));
        vis[start[0] as usize][start[1] as usize] = true;
        let mut cands = Vec::new();
        let dirs = [(1i32, 0i32), (-1, 0), (0, 1), (0, -1)];
        while let Some((r, c, d)) = q.pop_front() {
            if grid[r][c] >= low && grid[r][c] <= high {
                cands.push((d, grid[r][c], r as i32, c as i32));
            }
            for (dr, dc) in dirs {
                let nr = r as i32 + dr;
                let nc = c as i32 + dc;
                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let (nr, nc) = (nr as usize, nc as usize);
                    if !vis[nr][nc] && grid[nr][nc] != 0 {
                        vis[nr][nc] = true;
                        q.push_back((nr, nc, d + 1));
                    }
                }
            }
        }
        cands.sort_unstable();
        let k = (k as usize).min(cands.len());
        cands[..k].iter().map(|&(_, _, r, c)| vec![r, c]).collect()
    }
}
