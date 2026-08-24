// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

use std::collections::HashMap;

pub struct MyHashMap {
    data: HashMap<i32, i32>,
}

impl MyHashMap {
    pub fn new() -> Self {
        Self {
            data: HashMap::new(),
        }
    }

    pub fn put(&mut self, key: i32, value: i32) {
        self.data.insert(key, value);
    }

    pub fn get(&self, key: i32) -> i32 {
        *self.data.get(&key).unwrap_or(&-1)
    }

    pub fn remove(&mut self, key: i32) {
        self.data.remove(&key);
    }
}
