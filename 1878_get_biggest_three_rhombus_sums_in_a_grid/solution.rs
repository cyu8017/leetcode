// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

use std::collections::BTreeSet;

impl Solution {
    pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();
        let mut s1 = vec![vec![0i32; n + 2]; m + 1];
        let mut s2 = vec![vec![0i32; n + 2]; m + 1];
        for i in 1..=m {
            for j in 1..=n {
                let value = grid[i - 1][j - 1];
                s1[i][j] = s1[i - 1][j - 1] + value;
                s2[i][j] = s2[i - 1][j + 1] + value;
            }
        }
        let mut rhombus_sums = BTreeSet::new();
        for i in 1..=m {
            for j in 1..=n {
                let value = grid[i - 1][j - 1];
                let limit = (i - 1).min(m - i).min(j - 1).min(n - j);
                rhombus_sums.insert(value);
                for k in 1..=limit {
                    let a = s1[i + k][j] - s1[i][j - k];
                    let b = s1[i][j + k] - s1[i - k][j];
                    let c = s2[i][j - k] - s2[i - k][j];
                    let d = s2[i + k][j] - s2[i][j + k];
                    rhombus_sums.insert(
                        a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1],
                    );
                }
            }
        }
        rhombus_sums.into_iter().rev().take(3).collect()
    }
}
