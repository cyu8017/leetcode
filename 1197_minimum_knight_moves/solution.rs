// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

use std::collections::HashMap;

impl Solution {
    pub fn min_knight_moves(x: i32, y: i32) -> i32 {
        let mut memo = HashMap::new();
        fn dfs(mut a: i32, mut b: i32, memo: &mut HashMap<(i32, i32), i32>) -> i32 {
            if a < b {
                std::mem::swap(&mut a, &mut b);
            }
            if let Some(&v) = memo.get(&(a, b)) {
                return v;
            }
            if a + b == 0 {
                return 0;
            }
            if a + b == 2 {
                return 2;
            }
            let v = 1 + dfs((a - 1).abs(), (b - 2).abs(), memo)
                .min(dfs((a - 2).abs(), (b - 1).abs(), memo));
            memo.insert((a, b), v);
            v
        }
        dfs(x.abs(), y.abs(), &mut memo)
    }
}
