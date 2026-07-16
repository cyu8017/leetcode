// LeetCode 0346 - Moving Average from Data Stream
// https://leetcode.com/problems/moving-average-from-data-stream/

use std::collections::VecDeque;

struct MovingAverage {
    size: i32,
    values: VecDeque<i32>,
    total: i64,
}

impl MovingAverage {
    fn new(size: i32) -> Self {
        Self {
            size,
            values: VecDeque::new(),
            total: 0,
        }
    }

    fn next(&mut self, val: i32) -> f64 {
        self.values.push_back(val);
        self.total += val as i64;
        if self.values.len() as i32 > self.size {
            if let Some(front) = self.values.pop_front() {
                self.total -= front as i64;
            }
        }
        self.total as f64 / self.values.len() as f64
    }
}
