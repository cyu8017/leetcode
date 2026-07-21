// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

use std::collections::VecDeque;

pub struct MKAverage {
    m: usize,
    k: usize,
    stream: VecDeque<i32>,
}

impl MKAverage {
    pub fn new(m: i32, k: i32) -> Self {
        Self {
            m: m as usize,
            k: k as usize,
            stream: VecDeque::new(),
        }
    }

    pub fn add_element(&mut self, num: i32) {
        self.stream.push_back(num);
    }

    pub fn calculate_mk_average(&self) -> i32 {
        if self.stream.len() < self.m {
            return -1;
        }
        let start = self.stream.len() - self.m;
        let mut window: Vec<i32> = self.stream.iter().skip(start).copied().collect();
        window.sort_unstable();
        let middle = &window[self.k..window.len() - self.k];
        (middle.iter().map(|&x| x as i64).sum::<i64>() / middle.len() as i64) as i32
    }
}
