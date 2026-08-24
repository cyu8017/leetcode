// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

use std::collections::HashMap;

impl Solution {
    fn rotate(grid: &[Vec<i32>]) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut t = vec![vec![0; m]; n];
        for i in 0..m {
            for j in 0..n {
                t[j][i] = grid[i][j];
            }
        }
        t
    }

    fn check(g: &[Vec<i32>]) -> bool {
        let m = g.len();
        let n = g[0].len();
        let mut s1 = 0i64;
        let mut s2 = 0i64;
        let mut cnt1: HashMap<i64, i32> = HashMap::new();
        let mut cnt2: HashMap<i64, i32> = HashMap::new();
        for row in g {
            for &x in row {
                let v = x as i64;
                s2 += v;
                *cnt2.entry(v).or_insert(0) += 1;
            }
        }
        for i in 0..m - 1 {
            for &x in &g[i] {
                let v = x as i64;
                s1 += v;
                s2 -= v;
                *cnt1.entry(v).or_insert(0) += 1;
                *cnt2.entry(v).or_insert(0) -= 1;
            }
            if s1 == s2 {
                return true;
            }
            if s1 < s2 {
                let diff = s2 - s1;
                if *cnt2.get(&diff).unwrap_or(&0) > 0 {
                    if (m - i - 1 > 1 && n > 1)
                        || (i == m - 2 && (g[i + 1][0] as i64 == diff || g[i + 1][n - 1] as i64 == diff))
                        || (n == 1 && (g[i + 1][0] as i64 == diff || g[m - 1][0] as i64 == diff))
                    {
                        return true;
                    }
                }
            } else {
                let diff = s1 - s2;
                if *cnt1.get(&diff).unwrap_or(&0) > 0 {
                    if (i + 1 > 1 && n > 1)
                        || (i == 0 && (g[0][0] as i64 == diff || g[0][n - 1] as i64 == diff))
                        || (n == 1 && (g[0][0] as i64 == diff || g[i][0] as i64 == diff))
                    {
                        return true;
                    }
                }
            }
        }
        false
    }

    pub fn can_partition_grid(grid: Vec<Vec<i32>>) -> bool {
        Self::check(&grid) || Self::check(&Self::rotate(&grid))
    }
}
