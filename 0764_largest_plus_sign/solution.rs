// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

use std::collections::HashSet;

impl Solution {
    pub fn order_of_largest_plus_sign(n: i32, mines: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let banned: HashSet<usize> = mines
            .into_iter()
            .map(|mine| mine[0] as usize * n + mine[1] as usize)
            .collect();
        let mut arms = vec![vec![0; n]; n];
        let mut best = 0;
        for r in 0..n {
            let mut count = 0;
            for c in 0..n {
                count = if banned.contains(&(r * n + c)) { 0 } else { count + 1 };
                arms[r][c] = count;
            }
            count = 0;
            for c in (0..n).rev() {
                count = if banned.contains(&(r * n + c)) { 0 } else { count + 1 };
                arms[r][c] = arms[r][c].min(count);
            }
        }
        for c in 0..n {
            let mut count = 0;
            for r in 0..n {
                count = if banned.contains(&(r * n + c)) { 0 } else { count + 1 };
                arms[r][c] = arms[r][c].min(count);
            }
            count = 0;
            for r in (0..n).rev() {
                count = if banned.contains(&(r * n + c)) { 0 } else { count + 1 };
                arms[r][c] = arms[r][c].min(count);
                best = best.max(arms[r][c]);
            }
        }
        best
    }
}
