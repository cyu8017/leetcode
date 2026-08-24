// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

use std::collections::BTreeSet;

pub struct ExamRoom {
    n: i32,
    seats: BTreeSet<i32>,
}

impl ExamRoom {
    pub fn new(n: i32) -> Self {
        Self {
            n,
            seats: BTreeSet::new(),
        }
    }

    pub fn seat(&mut self) -> i32 {
        if self.seats.is_empty() {
            self.seats.insert(0);
            return 0;
        }
        let mut best_seat = 0;
        let first = *self.seats.iter().next().unwrap();
        let mut best_dist = first;
        let mut prev = first;
        for &cur in self.seats.iter().skip(1) {
            let dist = (cur - prev) / 2;
            if dist > best_dist {
                best_dist = dist;
                best_seat = prev + dist;
            }
            prev = cur;
        }
        let last = *self.seats.iter().next_back().unwrap();
        if self.n - 1 - last > best_dist {
            best_seat = self.n - 1;
        }
        self.seats.insert(best_seat);
        best_seat
    }

    pub fn leave(&mut self, p: i32) {
        self.seats.remove(&p);
    }
}
