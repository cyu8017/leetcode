struct Solution;
// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

use std::collections::HashMap;

impl Solution {
    pub fn least_bricks(wall: Vec<Vec<i32>>) -> i32 {
        let mut edges = HashMap::new();
        let mut best = 0;
        for row in &wall {
            let mut width = 0;
            for &brick in &row[..row.len().saturating_sub(1)] {
                width += brick;
                let count = edges.entry(width).or_insert(0);
                *count += 1;
                best = best.max(*count);
            }
        }
        wall.len() as i32 - best
    }
}

fn main() {}
