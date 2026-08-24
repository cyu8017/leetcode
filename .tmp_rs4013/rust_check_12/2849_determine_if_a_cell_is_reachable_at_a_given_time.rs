struct Solution;
// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

impl Solution {
    pub fn is_reachable_at_time(sx: i32, sy: i32, fx: i32, fy: i32, t: i32) -> bool {
        let need = (sx - fx).abs().max((sy - fy).abs());
        if need == 0 {
            return t != 1;
        }
        t >= need
    }
}

fn main() {}
