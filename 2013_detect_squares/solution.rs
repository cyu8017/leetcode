// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

use std::collections::HashMap;

pub struct DetectSquares {
    cnt: HashMap<(i32, i32), i32>,
}

impl DetectSquares {
    pub fn new() -> Self {
        Self {
            cnt: HashMap::new(),
        }
    }

    pub fn add(&mut self, point: Vec<i32>) {
        *self.cnt.entry((point[0], point[1])).or_insert(0) += 1;
    }

    pub fn count(&self, point: Vec<i32>) -> i32 {
        let (x, y) = (point[0], point[1]);
        let mut ans = 0;
        for (&(px, py), &c) in &self.cnt {
            if px == x || py == y {
                continue;
            }
            if (px - x).abs() != (py - y).abs() {
                continue;
            }
            ans += c * self.cnt.get(&(px, y)).unwrap_or(&0) * self.cnt.get(&(x, py)).unwrap_or(&0);
        }
        ans
    }
}
