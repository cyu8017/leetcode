// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

use std::collections::HashMap;

impl Solution {
    pub fn survived_robots_healths(
        positions: Vec<i32>,
        healths: Vec<i32>,
        directions: String,
    ) -> Vec<i32> {
        let n = positions.len();
        let dir = directions.as_bytes();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_unstable_by_key(|&i| positions[i]);
        let mut stack: Vec<(usize, i32, u8)> = Vec::new();
        for i in idx {
            let mut cur = (i, healths[i], dir[i]);
            while !stack.is_empty() && stack.last().unwrap().2 == b'R' && cur.2 == b'L' {
                let back = stack.last().unwrap().1;
                if back == cur.1 {
                    stack.pop();
                    cur.1 = 0;
                    break;
                } else if back > cur.1 {
                    stack.last_mut().unwrap().1 -= 1;
                    cur.1 = 0;
                    break;
                } else {
                    cur.1 -= 1;
                    stack.pop();
                }
            }
            if cur.1 > 0 {
                stack.push(cur);
            }
        }
        let alive: HashMap<usize, i32> = stack.into_iter().map(|(i, h, _)| (i, h)).collect();
        (0..n).filter_map(|i| alive.get(&i).copied()).collect()
    }
}
