#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3021 - Alice and Bob Playing Flower Game
// https://leetcode.com/problems/alice-and-bob-playing-flower-game/

impl Solution {
    pub fn flower_game(n: i32, m: i32) -> i64 {
        let a1 = (n as i64 + 1) / 2;
        let b1 = (m as i64 + 1) / 2;
        let a2 = n as i64 / 2;
        let b2 = m as i64 / 2;
        a1 * b2 + a2 * b1
    }
}
