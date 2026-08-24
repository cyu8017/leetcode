// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

use std::collections::{HashMap, HashSet};

pub struct StatisticsTracker {
    arr: Vec<i32>,
    sum: i64,
    freq: HashMap<i32, i32>,
    mode_freq: i32,
    modes: HashSet<i32>,
}

impl StatisticsTracker {
    pub fn new() -> Self {
        Self {
            arr: Vec::new(),
            sum: 0,
            freq: HashMap::new(),
            mode_freq: 0,
            modes: HashSet::new(),
        }
    }

    pub fn add_number(&mut self, num: i32) {
        self.arr.push(num);
        self.sum += num as i64;
        let f = {
            let e = self.freq.entry(num).or_insert(0);
            *e += 1;
            *e
        };
        if f > self.mode_freq {
            self.mode_freq = f;
            self.modes.clear();
            self.modes.insert(num);
        } else if f == self.mode_freq {
            self.modes.insert(num);
        }
    }

    pub fn remove_first(&mut self) {
        if self.arr.is_empty() {
            return;
        }
        let num = self.arr.remove(0);
        self.sum -= num as i64;
        if let Some(f) = self.freq.get_mut(&num) {
            *f -= 1;
            if *f == 0 {
                self.freq.remove(&num);
            }
        }
        self.mode_freq = 0;
        self.modes.clear();
        for (&v, &f) in &self.freq {
            if f > self.mode_freq {
                self.mode_freq = f;
                self.modes.clear();
                self.modes.insert(v);
            } else if f == self.mode_freq {
                self.modes.insert(v);
            }
        }
    }

    pub fn get_mean(&self) -> i32 {
        if self.arr.is_empty() {
            return 0;
        }
        (self.sum / self.arr.len() as i64) as i32
    }

    pub fn get_median(&self) -> i32 {
        let n = self.arr.len();
        let mut tmp = self.arr.clone();
        tmp.sort_unstable();
        if n % 2 == 1 {
            tmp[n / 2]
        } else {
            tmp[n / 2 - 1]
        }
    }

    pub fn get_mode(&self) -> i32 {
        let mut best = i64::MAX;
        for &v in &self.modes {
            if (v as i64) < best {
                best = v as i64;
            }
        }
        if best == i64::MAX {
            0
        } else {
            best as i32
        }
    }
}

fn main() {}
