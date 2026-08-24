struct Solution;
// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

use std::collections::HashMap;

impl Solution {
    pub fn is_there_a_path(grid: Vec<Vec<i32>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        if (m + n - 1) % 2 != 0 {
            return false;
        }
        let target = (m + n - 1) / 2;
        let mut memo: HashMap<(usize, usize, i32), bool> = HashMap::new();
        fn dfs(
            r: usize,
            c: usize,
            bal: i32,
            grid: &[Vec<i32>],
            target: i32,
            memo: &mut HashMap<(usize, usize, i32), bool>,
        ) -> bool {
            let m = grid.len();
            let n = grid[0].len();
            if r >= m || c >= n {
                return false;
            }
            let bal = bal + grid[r][c];
            if bal > target || bal + (m as i32 - 1 - r as i32) + (n as i32 - 1 - c as i32) < target {
                return false;
            }
            if r == m - 1 && c == n - 1 {
                return bal == target;
            }
            if let Some(&v) = memo.get(&(r, c, bal)) {
                return v;
            }
            let ok = dfs(r + 1, c, bal, grid, target, memo) || dfs(r, c + 1, bal, grid, target, memo);
            memo.insert((r, c, bal), ok);
            ok
        }
        dfs(0, 0, 0, &grid, target as i32, &mut memo)
    }
}

fn main() {}
