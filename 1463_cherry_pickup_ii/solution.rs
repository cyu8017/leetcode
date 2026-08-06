// LeetCode 1463 - Cherry Pickup II
// https://leetcode.com/problems/cherry-pickup-ii/

use std::collections::HashMap;

impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = HashMap::new();
        dp.insert((0usize, n - 1), grid[0][0] + if n > 1 { grid[0][n - 1] } else { 0 });
        for r in 1..m {
            let mut nxt = HashMap::new();
            for (&(a, b), &score) in &dp {
                for da in [-1i32, 0, 1] {
                    for db in [-1i32, 0, 1] {
                        let na = a as i32 + da;
                        let nb = b as i32 + db;
                        if na >= 0 && (na as usize) < n && nb >= 0 && (nb as usize) < n {
                            let (na, nb) = (na as usize, nb as usize);
                            let val = score + grid[r][na] + if na != nb { grid[r][nb] } else { 0 };
                            nxt.entry((na, nb))
                                .and_modify(|e| *e = (*e).max(val))
                                .or_insert(val);
                        }
                    }
                }
            }
            dp = nxt;
        }
        *dp.values().max().unwrap_or(&0)
    }
}
