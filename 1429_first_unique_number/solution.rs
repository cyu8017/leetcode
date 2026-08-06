// LeetCode 1429 - First Unique Number
// https://leetcode.com/problems/first-unique-number/

use std::collections::{HashMap, VecDeque};

struct FirstUnique {
    counts: HashMap<i32, i32>,
    unique: VecDeque<i32>,
}

impl FirstUnique {
    fn new(nums: Vec<i32>) -> Self {
        let mut s = Self {
            counts: HashMap::new(),
            unique: VecDeque::new(),
        };
        for value in nums {
            s.add(value);
        }
        s
    }

    fn show_first_unique(&mut self) -> i32 {
        while let Some(&front) = self.unique.front() {
            if self.counts[&front] == 1 {
                return front;
            }
            self.unique.pop_front();
        }
        -1
    }

    fn add(&mut self, value: i32) {
        let c = self.counts.entry(value).or_insert(0);
        *c += 1;
        if *c == 1 {
            self.unique.push_back(value);
        }
    }
}
