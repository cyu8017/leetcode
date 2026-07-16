// LeetCode 0359 - Logger Rate Limiter
// https://leetcode.com/problems/logger-rate-limiter/

use std::collections::HashMap;

struct Logger {
    last_printed: HashMap<String, i32>,
}

impl Logger {
    fn new() -> Self {
        Self {
            last_printed: HashMap::new(),
        }
    }

    fn should_print_message(&mut self, timestamp: i32, message: String) -> bool {
        match self.last_printed.get(&message) {
            Some(last) if timestamp - last < 10 => false,
            _ => {
                self.last_printed.insert(message, timestamp);
                true
            }
        }
    }
}
