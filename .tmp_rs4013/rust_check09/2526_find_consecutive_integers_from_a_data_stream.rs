// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

pub struct DataStream {
    value: i32,
    k: i32,
    streak: i32,
}

impl DataStream {
    pub fn new(value: i32, k: i32) -> Self {
        Self {
            value,
            k,
            streak: 0,
        }
    }

    pub fn consec(&mut self, num: i32) -> bool {
        if num == self.value {
            self.streak += 1;
        } else {
            self.streak = 0;
        }
        self.streak >= self.k
    }
}

fn main() {}
