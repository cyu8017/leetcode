// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn largest_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut sizes = HashMap::from([(0, 0)]);
        let mut island_id = 2;
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] == 1 {
                    let sz = Self::dfs(&mut grid, i as i32, j as i32, island_id, n);
                    sizes.insert(island_id, sz);
                    island_id += 1;
                }
            }
        }
        let mut ans = *sizes.values().max().unwrap_or(&0);
        let dr = [1i32, -1, 0, 0];
        let dc = [0i32, 0, 1, -1];
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] != 0 {
                    continue;
                }
                let mut seen = HashSet::new();
                let mut total = 1;
                for k in 0..4 {
                    let ni = i as i32 + dr[k];
                    let nj = j as i32 + dc[k];
                    if ni >= 0 && ni < n as i32 && nj >= 0 && nj < n as i32 {
                        let iid = grid[ni as usize][nj as usize];
                        if iid > 1 && seen.insert(iid) {
                            total += sizes.get(&iid).copied().unwrap_or(0);
                        }
                    }
                }
                ans = ans.max(total);
            }
        }
        ans
    }

    fn dfs(grid: &mut [Vec<i32>], r: i32, c: i32, iid: i32, n: usize) -> i32 {
        if r < 0 || r >= n as i32 || c < 0 || c >= n as i32 || grid[r as usize][c as usize] != 1 {
            return 0;
        }
        grid[r as usize][c as usize] = iid;
        1 + Self::dfs(grid, r + 1, c, iid, n)
            + Self::dfs(grid, r - 1, c, iid, n)
            + Self::dfs(grid, r, c + 1, iid, n)
            + Self::dfs(grid, r, c - 1, iid, n)
    }
}
