// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

use std::collections::HashMap;
use std::time::{Duration, Instant};

pub struct TimeLimitedCache {
    data: HashMap<i32, (i32, Instant)>,
}

impl TimeLimitedCache {
    pub fn new() -> Self {
        Self {
            data: HashMap::new(),
        }
    }

    pub fn set(&mut self, key: i32, value: i32, duration: i32) -> bool {
        let now = Instant::now();
        let alive = self
            .data
            .get(&key)
            .map(|(_, expire)| *expire > now)
            .unwrap_or(false);
        self.data.insert(
            key,
            (value, now + Duration::from_millis(duration.max(0) as u64)),
        );
        alive
    }

    pub fn get(&self, key: i32) -> i32 {
        let now = Instant::now();
        match self.data.get(&key) {
            Some((value, expire)) if *expire > now => *value,
            _ => -1,
        }
    }

    pub fn count(&mut self) -> i32 {
        let now = Instant::now();
        self.data.retain(|_, (_, expire)| *expire > now);
        self.data.len() as i32
    }
}
