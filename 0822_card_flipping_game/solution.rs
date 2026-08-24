// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

use std::collections::HashSet;

impl Solution {
    pub fn flipgame(fronts: Vec<i32>, backs: Vec<i32>) -> i32 {
        let mut same = HashSet::new();
        for i in 0..fronts.len() {
            if fronts[i] == backs[i] {
                same.insert(fronts[i]);
            }
        }
        let mut best = i32::MAX;
        for &x in fronts.iter().chain(backs.iter()) {
            if !same.contains(&x) {
                best = best.min(x);
            }
        }
        if best == i32::MAX {
            0
        } else {
            best
        }
    }
}
