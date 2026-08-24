// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

use std::collections::HashMap;

pub struct LogSystem {
    logs: Vec<(i32, String)>,
    granularity_index: HashMap<String, usize>,
}

impl LogSystem {
    pub fn new() -> Self {
        let mut granularity_index = HashMap::new();
        granularity_index.insert("Year".to_string(), 4);
        granularity_index.insert("Month".to_string(), 7);
        granularity_index.insert("Day".to_string(), 10);
        granularity_index.insert("Hour".to_string(), 13);
        granularity_index.insert("Minute".to_string(), 16);
        granularity_index.insert("Second".to_string(), 19);
        Self {
            logs: Vec::new(),
            granularity_index,
        }
    }

    pub fn put(&mut self, id: i32, timestamp: String) {
        self.logs.push((id, timestamp));
    }

    pub fn retrieve(&self, start: String, end: String, granularity: String) -> Vec<i32> {
        let index = self.granularity_index[&granularity];
        let start_key = &start[..index];
        let end_key = &end[..index];
        let mut matched = Vec::new();
        for (log_id, timestamp) in &self.logs {
            let key = &timestamp[..index];
            if start_key <= key && key <= end_key {
                matched.push((timestamp.clone(), *log_id));
            }
        }
        matched.sort();
        matched.into_iter().map(|(_, id)| id).collect()
    }
}
