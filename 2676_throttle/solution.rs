// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

use std::time::{Duration, Instant};

impl Solution {
    pub fn throttle(f: impl Fn(), t: i32) -> impl FnMut() {
        let mut last = Instant::now() - Duration::from_secs(86400);
        move || {
            let now = Instant::now();
            if now.duration_since(last).as_millis() as i64 >= t as i64 {
                last = now;
                f();
            }
        }
    }
}
