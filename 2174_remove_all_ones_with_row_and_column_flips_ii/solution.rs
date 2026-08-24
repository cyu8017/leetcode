// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

impl Solution {
    pub fn remove_ones(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut ones = Vec::new();
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    ones.push((i, j));
                }
            }
        }
        if ones.is_empty() {
            return 0;
        }
        let mut ans = (m + n) as i32;
        fn dfs(
            idx: usize,
            flips: i32,
            grid: &mut Vec<Vec<i32>>,
            ones: &[(usize, usize)],
            m: usize,
            n: usize,
            ans: &mut i32,
        ) {
            if flips >= *ans {
                return;
            }
            let mut idx = idx;
            while idx < ones.len() && grid[ones[idx].0][ones[idx].1] == 0 {
                idx += 1;
            }
            if idx == ones.len() {
                *ans = flips;
                return;
            }
            let (r, c) = ones[idx];
            let mut changed = Vec::new();
            for j in 0..n {
                if grid[r][j] == 1 {
                    grid[r][j] = 0;
                    changed.push((r, j));
                }
            }
            dfs(idx + 1, flips + 1, grid, ones, m, n, ans);
            for (i, j) in changed {
                grid[i][j] = 1;
            }
            let mut changed = Vec::new();
            for i in 0..m {
                if grid[i][c] == 1 {
                    grid[i][c] = 0;
                    changed.push((i, c));
                }
            }
            dfs(idx + 1, flips + 1, grid, ones, m, n, ans);
            for (i, j) in changed {
                grid[i][j] = 1;
            }
        }
        let mut grid = grid;
        dfs(0, 0, &mut grid, &ones, m, n, &mut ans);
        ans
    }
}
