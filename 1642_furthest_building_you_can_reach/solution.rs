// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

use std::collections::BinaryHeap;

impl Solution {
    pub fn furthest_building(heights: Vec<i32>, mut bricks: i32, ladders: i32) -> i32 {
        let mut climbs = BinaryHeap::new();
        for i in 0..heights.len() - 1 {
            let d = heights[i + 1] - heights[i];
            if d <= 0 {
                continue;
            }
            climbs.push(-d);
            if climbs.len() > ladders as usize {
                bricks += climbs.pop().unwrap();
            }
            if bricks < 0 {
                return i as i32;
            }
        }
        (heights.len() - 1) as i32
    }
}
