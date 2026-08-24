// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        let dead: HashSet<String> = deadends.into_iter().collect();
        if dead.contains("0000") {
            return -1;
        }
        let mut q = VecDeque::new();
        let mut seen = HashSet::new();
        seen.insert("0000".to_string());
        q.push_back(("0000".to_string(), 0));
        while let Some((state, steps)) = q.pop_front() {
            if state == target {
                return steps;
            }
            let bytes = state.into_bytes();
            for i in 0..4 {
                let digit = bytes[i] - b'0';
                for delta in [-1i32, 1] {
                    let mut nxt = bytes.clone();
                    nxt[i] = b'0' + ((digit as i32 + delta + 10) % 10) as u8;
                    let nxt = String::from_utf8(nxt).unwrap();
                    if !seen.contains(&nxt) && !dead.contains(&nxt) {
                        seen.insert(nxt.clone());
                        q.push_back((nxt, steps + 1));
                    }
                }
            }
        }
        -1
    }
}
