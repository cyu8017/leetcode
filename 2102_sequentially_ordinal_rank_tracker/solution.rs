// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

#[derive(Eq, PartialEq)]
struct Loc {
    score: i32,
    name: String,
}

impl Ord for Loc {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.score
            .cmp(&other.score)
            .then_with(|| other.name.cmp(&self.name))
    }
}

impl PartialOrd for Loc {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

pub struct SORTracker {
    best: BinaryHeap<Reverse<Loc>>,
    rest: BinaryHeap<Loc>,
    k: usize,
}

impl SORTracker {
    pub fn new() -> Self {
        Self {
            best: BinaryHeap::new(),
            rest: BinaryHeap::new(),
            k: 0,
        }
    }

    pub fn add(&mut self, name: String, score: i32) {
        self.best.push(Reverse(Loc { score, name }));
        if self.best.len() > self.k {
            if let Some(Reverse(loc)) = self.best.pop() {
                self.rest.push(loc);
            }
        }
    }

    pub fn get(&mut self) -> String {
        self.k += 1;
        if let Some(loc) = self.rest.pop() {
            self.best.push(Reverse(loc));
        }
        self.best.peek().map(|Reverse(loc)| loc.name.clone()).unwrap_or_default()
    }
}
