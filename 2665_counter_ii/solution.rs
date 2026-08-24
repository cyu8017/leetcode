// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

pub struct CounterII {
    init: i32,
    cur: i32,
}

impl CounterII {
    pub fn new(init: i32) -> Self {
        Self { init, cur: init }
    }

    pub fn increment(&mut self) -> i32 {
        self.cur += 1;
        self.cur
    }

    pub fn decrement(&mut self) -> i32 {
        self.cur -= 1;
        self.cur
    }

    pub fn reset(&mut self) -> i32 {
        self.cur = self.init;
        self.cur
    }
}

impl Solution {
    pub fn create_counter(init: i32) -> CounterII {
        CounterII::new(init)
    }
}
