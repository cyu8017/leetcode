// LeetCode 0379 - Design Phone Directory
// https://leetcode.com/problems/design-phone-directory/

use std::collections::BTreeSet;

struct PhoneDirectory {
    available: BTreeSet<i32>,
}

impl PhoneDirectory {
    fn new(max_numbers: i32) -> Self {
        Self {
            available: (0..max_numbers).collect(),
        }
    }

    fn get(&mut self) -> i32 {
        if let Some(&number) = self.available.iter().next() {
            self.available.remove(&number);
            number
        } else {
            -1
        }
    }

    fn check(&self, number: i32) -> bool {
        self.available.contains(&number)
    }

    fn release(&mut self, number: i32) {
        self.available.insert(number);
    }
}
