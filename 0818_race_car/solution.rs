// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn racecar(target: i32) -> i32 {
        fn key(pos: i32, speed: i32) -> i64 {
            ((pos as i64) << 20) ^ (speed as u32 as i64 & 0xfffff)
        }
        let mut queue = VecDeque::new();
        queue.push_back((0i32, 1i32, 0i32));
        let mut seen = HashSet::new();
        seen.insert(key(0, 1));
        while let Some((pos, speed, steps)) = queue.pop_front() {
            if pos == target {
                return steps;
            }
            let nxt_pos = pos + speed;
            let nxt_speed = speed * 2;
            if !seen.contains(&key(nxt_pos, nxt_speed)) && nxt_pos.abs() < target * 2 {
                seen.insert(key(nxt_pos, nxt_speed));
                queue.push_back((nxt_pos, nxt_speed, steps + 1));
            }
            let rev_speed = if speed > 0 { -1 } else { 1 };
            if seen.insert(key(pos, rev_speed)) {
                queue.push_back((pos, rev_speed, steps + 1));
            }
        }
        -1
    }
}
