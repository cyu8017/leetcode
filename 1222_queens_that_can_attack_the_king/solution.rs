// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

use std::collections::HashSet;

impl Solution {
    pub fn queens_attackthe_king(queens: Vec<Vec<i32>>, king: Vec<i32>) -> Vec<Vec<i32>> {
        let occupied: HashSet<(i32, i32)> =
            queens.iter().map(|q| (q[0], q[1])).collect();
        let mut ans = Vec::new();
        for dr in -1..=1 {
            for dc in -1..=1 {
                if dr == 0 && dc == 0 {
                    continue;
                }
                let mut r = king[0] + dr;
                let mut c = king[1] + dc;
                while (0..8).contains(&r) && (0..8).contains(&c) {
                    if occupied.contains(&(r, c)) {
                        ans.push(vec![r, c]);
                        break;
                    }
                    r += dr;
                    c += dc;
                }
            }
        }
        ans
    }
}
