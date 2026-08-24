// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

use std::collections::HashSet;

pub struct MyHashSet {
    data: HashSet<i32>,
}

impl MyHashSet {
    pub fn new() -> Self {
        Self {
            data: HashSet::new(),
        }
    }

    pub fn add(&mut self, key: i32) {
        self.data.insert(key);
    }

    pub fn remove(&mut self, key: i32) {
        self.data.remove(&key);
    }

    pub fn contains(&self, key: i32) -> bool {
        self.data.contains(&key)
    }
}
