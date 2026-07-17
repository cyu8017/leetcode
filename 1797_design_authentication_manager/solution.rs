// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

use std::collections::HashMap;

struct AuthenticationManager {
    ttl: i32,
    tokens: HashMap<String, i32>,
}

impl AuthenticationManager {
    fn new(time_to_live: i32) -> Self {
        AuthenticationManager {
            ttl: time_to_live,
            tokens: HashMap::new(),
        }
    }

    fn generate(&mut self, token_id: String, current_time: i32) {
        self.tokens.insert(token_id, current_time + self.ttl);
    }

    fn renew(&mut self, token_id: String, current_time: i32) {
        if let Some(exp) = self.tokens.get_mut(&token_id) {
            if *exp > current_time {
                *exp = current_time + self.ttl;
            }
        }
    }

    fn count_unexpired_tokens(&self, current_time: i32) -> i32 {
        self.tokens.values().filter(|&&exp| exp > current_time).count() as i32
    }
}
