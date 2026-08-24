// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

use std::collections::VecDeque;

pub struct RecentCounter {
    q: VecDeque<i32>,
}

impl RecentCounter {
    pub fn new() -> Self {
        Self { q: VecDeque::new() }
    }

    pub fn ping(&mut self, t: i32) -> i32 {
        self.q.push_back(t);
        while self.q.front().map_or(false, |&x| x < t - 3000) {
            self.q.pop_front();
        }
        self.q.len() as i32
    }
}
