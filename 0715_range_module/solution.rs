// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

pub struct RangeModule {
    intervals: Vec<(i32, i32)>,
}

impl RangeModule {
    pub fn new() -> Self {
        Self {
            intervals: Vec::new(),
        }
    }

    pub fn add_range(&mut self, mut left: i32, mut right: i32) {
        let mut next = Vec::new();
        let mut placed = false;
        for &(start, end) in &self.intervals {
            if end < left {
                next.push((start, end));
            } else if right < start {
                if !placed {
                    next.push((left, right));
                    placed = true;
                }
                next.push((start, end));
            } else {
                left = left.min(start);
                right = right.max(end);
            }
        }
        if !placed {
            next.push((left, right));
        }
        self.intervals = next;
    }

    pub fn query_range(&self, left: i32, right: i32) -> bool {
        for &(start, end) in &self.intervals {
            if start <= left && right <= end {
                return true;
            }
            if end >= right {
                break;
            }
        }
        false
    }

    pub fn remove_range(&mut self, left: i32, right: i32) {
        let mut next = Vec::new();
        for &(start, end) in &self.intervals {
            if end <= left || right <= start {
                next.push((start, end));
            } else {
                if start < left {
                    next.push((start, left));
                }
                if right < end {
                    next.push((right, end));
                }
            }
        }
        self.intervals = next;
    }
}
