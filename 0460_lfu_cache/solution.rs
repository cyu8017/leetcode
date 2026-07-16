// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

use std::collections::HashMap;

pub struct LFUCache {
    capacity: i32,
    min_freq: i32,
    key_values: HashMap<i32, i32>,
    key_freqs: HashMap<i32, i32>,
    freq_keys: HashMap<i32, Vec<i32>>,
}

impl LFUCache {
    pub fn new(capacity: i32) -> Self {
        Self {
            capacity,
            min_freq: 0,
            key_values: HashMap::new(),
            key_freqs: HashMap::new(),
            freq_keys: HashMap::new(),
        }
    }

    fn touch(&mut self, key: i32) {
        let freq = self.key_freqs[key];
        {
            let bucket = self.freq_keys.get_mut(&freq).unwrap();
            if let Some(index) = bucket.iter().position(|&value| value == key) {
                bucket.remove(index);
            }
        }
        if self.freq_keys.get(&freq).is_some_and(|bucket| bucket.is_empty()) && freq == self.min_freq
        {
            self.min_freq += 1;
        }
        self.key_freqs.insert(key, freq + 1);
        self.freq_keys.entry(freq + 1).or_default().push(key);
    }

    pub fn get(&mut self, key: i32) -> i32 {
        if !self.key_values.contains_key(&key) {
            return -1;
        }
        self.touch(key);
        self.key_values[&key]
    }

    pub fn put(&mut self, key: i32, value: i32) {
        if self.capacity == 0 {
            return;
        }
        if self.key_values.contains_key(&key) {
            self.key_values.insert(key, value);
            self.touch(key);
            return;
        }
        if self.key_values.len() as i32 >= self.capacity {
            let evict = self.freq_keys.get_mut(&self.min_freq).unwrap().remove(0);
            self.key_values.remove(&evict);
            self.key_freqs.remove(&evict);
        }
        self.key_values.insert(key, value);
        self.key_freqs.insert(key, 1);
        self.freq_keys.entry(1).or_default().push(key);
        self.min_freq = 1;
    }
}
