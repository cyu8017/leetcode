// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

pub struct RLEIterator {
    enc: Vec<i32>,
    i: usize,
}

impl RLEIterator {
    pub fn new(encoding: Vec<i32>) -> Self {
        Self { enc: encoding, i: 0 }
    }

    pub fn next(&mut self, mut n: i32) -> i32 {
        while self.i < self.enc.len() {
            if self.enc[self.i] >= n {
                self.enc[self.i] -= n;
                return self.enc[self.i + 1];
            }
            n -= self.enc[self.i];
            self.i += 2;
        }
        -1
    }
}
