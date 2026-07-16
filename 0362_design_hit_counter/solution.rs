// LeetCode 0362 - Design Hit Counter
// https://leetcode.com/problems/design-hit-counter/

use std::collections::VecDeque;

struct HitCounter {
    hits: VecDeque<i32>,
}

impl HitCounter {
    fn new() -> Self {
        Self {
            hits: VecDeque::new(),
        }
    }

    fn hit(&mut self, timestamp: i32) {
        self.hits.push_back(timestamp);
    }

    fn get_hits(&mut self, timestamp: i32) -> i32 {
        while let Some(front) = self.hits.front() {
            if *front <= timestamp - 300 {
                self.hits.pop_front();
            } else {
                break;
            }
        }
        self.hits.len() as i32
    }
}
