// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

use std::collections::BTreeMap;

pub struct MyCalendarThree {
    delta: BTreeMap<i32, i32>,
}

impl MyCalendarThree {
    pub fn new() -> Self {
        Self {
            delta: BTreeMap::new(),
        }
    }

    pub fn book(&mut self, start_time: i32, end_time: i32) -> i32 {
        *self.delta.entry(start_time).or_insert(0) += 1;
        *self.delta.entry(end_time).or_insert(0) -= 1;
        let mut current = 0;
        let mut best = 0;
        for &change in self.delta.values() {
            current += change;
            best = best.max(current);
        }
        best
    }
}
