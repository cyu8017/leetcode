struct Solution;
// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

use std::collections::HashMap;

impl Solution {
    pub fn len_of_v_diagonal(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]];
        let next_dir = [1, 2, 3, 0];
        let mut ans = 0;
        let mut memo: HashMap<(i32, i32, i32, i32, i32), i32> = HashMap::new();
        fn dfs(
            i: i32,
            j: i32,
            d: usize,
            turned: i32,
            expect: i32,
            grid: &[Vec<i32>],
            dirs: &[[i32; 2]; 4],
            next_dir: &[usize; 4],
            memo: &mut HashMap<(i32, i32, i32, i32, i32), i32>,
        ) -> i32 {
            let m = grid.len() as i32;
            let n = grid[0].len() as i32;
            if i < 0 || j < 0 || i >= m || j >= n || grid[i as usize][j as usize] != expect {
                return 0;
            }
            let key = (i, j, d as i32, turned, expect);
            if let Some(&v) = memo.get(&key) {
                return v;
            }
            let ni = i + dirs[d][0];
            let nj = j + dirs[d][1];
            let nx = if expect == 2 { 0 } else { 2 };
            let mut best = 1 + dfs(ni, nj, d, turned, nx, grid, dirs, next_dir, memo);
            if turned == 0 {
                let nd = next_dir[d];
                let ti = i + dirs[nd][0];
                let tj = j + dirs[nd][1];
                let cand = 1 + dfs(ti, tj, nd, 1, nx, grid, dirs, next_dir, memo);
                if cand > best {
                    best = cand;
                }
            }
            memo.insert(key, best);
            best
        }
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] != 1 {
                    continue;
                }
                for d in 0..4 {
                    let ni = i as i32 + dirs[d][0];
                    let nj = j as i32 + dirs[d][1];
                    let best = 1 + dfs(
                        ni, nj, d, 0, 2, &grid, &dirs, &next_dir, &mut memo,
                    );
                    if best > ans {
                        ans = best;
                    }
                }
                if ans < 1 {
                    ans = 1;
                }
            }
        }
        ans
    }
}

fn main() {}
