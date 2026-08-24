// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

use std::collections::HashMap;

pub struct FreqStack {
    freq: HashMap<i32, i32>,
    group: HashMap<i32, Vec<i32>>,
    maxfreq: i32,
}

impl FreqStack {
    pub fn new() -> Self {
        Self {
            freq: HashMap::new(),
            group: HashMap::new(),
            maxfreq: 0,
        }
    }

    pub fn push(&mut self, val: i32) {
        let f = self.freq.entry(val).or_insert(0);
        *f += 1;
        let f = *f;
        self.maxfreq = self.maxfreq.max(f);
        self.group.entry(f).or_default().push(val);
    }

    pub fn pop(&mut self) -> i32 {
        let stack = self.group.get_mut(&self.maxfreq).unwrap();
        let val = stack.pop().unwrap();
        *self.freq.get_mut(&val).unwrap() -= 1;
        if stack.is_empty() {
            self.maxfreq -= 1;
        }
        val
    }
}
