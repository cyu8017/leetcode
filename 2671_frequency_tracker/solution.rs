// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

use std::collections::HashMap;

pub struct FrequencyTracker {
    freq: HashMap<i32, i32>,
    count: HashMap<i32, i32>,
}

impl FrequencyTracker {
    pub fn new() -> Self {
        Self {
            freq: HashMap::new(),
            count: HashMap::new(),
        }
    }

    pub fn add(&mut self, number: i32) {
        let old = *self.freq.get(&number).unwrap_or(&0);
        if old > 0 {
            *self.count.entry(old).or_insert(0) -= 1;
        }
        self.freq.insert(number, old + 1);
        *self.count.entry(old + 1).or_insert(0) += 1;
    }

    pub fn delete_one(&mut self, number: i32) {
        let old = *self.freq.get(&number).unwrap_or(&0);
        if old == 0 {
            return;
        }
        *self.count.entry(old).or_insert(0) -= 1;
        self.freq.insert(number, old - 1);
        if old - 1 > 0 {
            *self.count.entry(old - 1).or_insert(0) += 1;
        }
    }

    pub fn has_frequency(&self, frequency: i32) -> bool {
        *self.count.get(&frequency).unwrap_or(&0) > 0
    }
}
