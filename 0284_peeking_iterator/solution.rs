// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

struct Iterator {
    values: Vec<i32>,
    index: usize,
}

impl Iterator {
    fn new(values: Vec<i32>) -> Self {
        Self { values, index: 0 }
    }

    fn next(&mut self) -> i32 {
        let value = self.values[self.index];
        self.index += 1;
        value
    }

    fn has_next(&self) -> bool {
        self.index < self.values.len()
    }
}

struct PeekingIterator {
    iterator: Iterator,
    peeked: i32,
    has_peeked: bool,
}

impl PeekingIterator {
    fn new(mut iterator: Iterator) -> Self {
        Self {
            iterator,
            peeked: 0,
            has_peeked: false,
        }
    }

    fn peek(&mut self) -> i32 {
        if !self.has_peeked {
            self.peeked = self.iterator.next();
            self.has_peeked = true;
        }
        self.peeked
    }

    fn next(&mut self) -> i32 {
        if self.has_peeked {
            self.has_peeked = false;
            return self.peeked;
        }
        self.iterator.next()
    }

    fn has_next(&self) -> bool {
        self.has_peeked || self.iterator.has_next()
    }
}
