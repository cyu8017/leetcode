// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

use std::collections::HashMap;

pub struct TimeMap {
    store: HashMap<String, Vec<(i32, String)>>,
}

impl TimeMap {
    pub fn new() -> Self {
        Self {
            store: HashMap::new(),
        }
    }

    pub fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.store.entry(key).or_default().push((timestamp, value));
    }

    pub fn get(&self, key: String, timestamp: i32) -> String {
        let Some(arr) = self.store.get(&key) else {
            return String::new();
        };
        let mut lo = 0;
        let mut hi = arr.len();
        while lo < hi {
            let mid = (lo + hi) / 2;
            if arr[mid].0 <= timestamp {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        if lo == 0 {
            String::new()
        } else {
            arr[lo - 1].1.clone()
        }
    }
}
