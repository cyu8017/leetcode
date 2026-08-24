// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

pub struct InfiniteStream {
    bits: Vec<i32>,
    i: usize,
}

impl InfiniteStream {
    pub fn new(bits: Vec<i32>) -> Self {
        Self { bits, i: 0 }
    }
    pub fn next(&mut self) -> i32 {
        let v = self.bits[self.i];
        self.i += 1;
        v
    }
}

impl Solution {
    pub fn find_pattern(stream: &mut InfiniteStream, pattern: Vec<i32>) -> i32 {
        let mut a = 0;
        let mut b = 0;
        let m = pattern.len();
        let half = m >> 1;
        let mask1 = if half == 0 { 0 } else { (1 << half) - 1 };
        let mask2 = (1 << (m - half)) - 1;
        for i in 0..half {
            a |= pattern[i] << (half - 1 - i);
        }
        for i in half..m {
            b |= pattern[i] << (m - 1 - i);
        }
        let mut x = 0;
        let mut y = 0;
        let mut i = 1;
        loop {
            let mut v = stream.next();
            y = y << 1 | v;
            v = (y >> (m - half)) & 1;
            y &= mask2;
            x = x << 1 | v;
            x &= mask1;
            if i >= m as i32 && a == x && b == y {
                return i - m as i32;
            }
            i += 1;
        }
    }
}
