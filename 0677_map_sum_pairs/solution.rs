// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

use std::collections::HashMap;

pub struct MapSum {
    values: HashMap<String, i32>,
    prefix_sums: HashMap<String, i32>,
}

impl MapSum {
    pub fn new() -> Self {
        Self {
            values: HashMap::new(),
            prefix_sums: HashMap::new(),
        }
    }

    pub fn insert(&mut self, key: String, val: i32) {
        let delta = val - self.values.get(&key).copied().unwrap_or(0);
        self.values.insert(key.clone(), val);
        for i in 1..=key.len() {
            *self.prefix_sums.entry(key[..i].to_string()).or_insert(0) += delta;
        }
    }

    pub fn sum(&self, prefix: String) -> i32 {
        self.prefix_sums.get(&prefix).copied().unwrap_or(0)
    }
}
