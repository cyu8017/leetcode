// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

use std::collections::VecDeque;

pub struct FrontMiddleBackQueue {
    l: VecDeque<i32>,
    r: VecDeque<i32>,
}

impl FrontMiddleBackQueue {
    pub fn new() -> Self {
        Self {
            l: VecDeque::new(),
            r: VecDeque::new(),
        }
    }

    fn bal(&mut self) {
        while self.l.len() > self.r.len() + 1 {
            self.r.push_front(self.l.pop_back().unwrap());
        }
        while self.r.len() > self.l.len() {
            self.l.push_back(self.r.pop_front().unwrap());
        }
    }

    pub fn push_front(&mut self, val: i32) {
        self.l.push_front(val);
        self.bal();
    }

    pub fn push_middle(&mut self, val: i32) {
        if self.l.len() > self.r.len() {
            self.r.push_front(self.l.pop_back().unwrap());
        }
        self.l.push_back(val);
    }

    pub fn push_back(&mut self, val: i32) {
        self.r.push_back(val);
        self.bal();
    }

    pub fn pop_front(&mut self) -> i32 {
        if self.l.is_empty() {
            return -1;
        }
        let v = self.l.pop_front().unwrap();
        self.bal();
        v
    }

    pub fn pop_middle(&mut self) -> i32 {
        if self.l.is_empty() {
            return -1;
        }
        let v = self.l.pop_back().unwrap();
        self.bal();
        v
    }

    pub fn pop_back(&mut self) -> i32 {
        if self.l.is_empty() {
            return -1;
        }
        let v = if !self.r.is_empty() {
            self.r.pop_back().unwrap()
        } else {
            self.l.pop_back().unwrap()
        };
        self.bal();
        v
    }
}
