// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut freq = HashMap::new();
        for i in 0..n {
            *freq.entry(grid[i].clone()).or_insert(0) += 1;
        }
        let mut ans = 0;
        for j in 0..n {
            let col: Vec<i32> = (0..n).map(|i| grid[i][j]).collect();
            ans += freq.get(&col).copied().unwrap_or(0);
        }
        ans
    }
}
