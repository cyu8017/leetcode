// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

impl Solution {
    pub fn find_path(grid: Vec<Vec<i32>>, _k: i32) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut st: u64 = 0;
        let mut path: Vec<Vec<i32>> = Vec::new();
        let dirs = [-1i32, 0, 1, 0, -1];
        fn f(i: usize, j: usize, n: usize) -> usize {
            i * n + j
        }
        fn dfs(
            i: usize,
            j: usize,
            mut v: i32,
            m: usize,
            n: usize,
            grid: &[Vec<i32>],
            dirs: &[i32],
            st: &mut u64,
            path: &mut Vec<Vec<i32>>,
        ) -> bool {
            path.push(vec![i as i32, j as i32]);
            if path.len() == m * n {
                return true;
            }
            let idx = f(i, j, n);
            *st |= 1u64 << idx;
            if grid[i][j] == v {
                v += 1;
            }
            for t in 0..4 {
                let x = i as i32 + dirs[t];
                let y = j as i32 + dirs[t + 1];
                if x >= 0 && x < m as i32 && y >= 0 && y < n as i32 {
                    let (x, y) = (x as usize, y as usize);
                    let idx2 = f(x, y, n);
                    if ((*st >> idx2) & 1) == 0 && (grid[x][y] == 0 || grid[x][y] == v) {
                        if dfs(x, y, v, m, n, grid, dirs, st, path) {
                            return true;
                        }
                    }
                }
            }
            path.pop();
            *st ^= 1u64 << idx;
            false
        }
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 0 || grid[i][j] == 1 {
                    if dfs(i, j, 1, m, n, &grid, &dirs, &mut st, &mut path) {
                        return path;
                    }
                    path.clear();
                    st = 0;
                }
            }
        }
        vec![]
    }
}
