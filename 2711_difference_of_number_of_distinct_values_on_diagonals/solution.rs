// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

use std::collections::HashSet;

impl Solution {
    pub fn difference_of_distinct_values(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                let mut top = HashSet::new();
                let mut bot = HashSet::new();
                let mut r = i as i32 - 1;
                let mut c = j as i32 - 1;
                while r >= 0 && c >= 0 {
                    top.insert(grid[r as usize][c as usize]);
                    r -= 1;
                    c -= 1;
                }
                r = i as i32 + 1;
                c = j as i32 + 1;
                while r < m as i32 && c < n as i32 {
                    bot.insert(grid[r as usize][c as usize]);
                    r += 1;
                    c += 1;
                }
                ans[i][j] = (top.len() as i32 - bot.len() as i32).abs();
            }
        }
        ans
    }
}
