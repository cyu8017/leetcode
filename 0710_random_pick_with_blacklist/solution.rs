// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

use std::collections::{HashMap, HashSet};

pub struct Solution {
    size: i32,
    mapping: HashMap<i32, i32>,
    seed: u64,
}

impl Solution {
    pub fn new(n: i32, blacklist: Vec<i32>) -> Self {
        let size = n - blacklist.len() as i32;
        let black: HashSet<i32> = blacklist.iter().copied().collect();
        let mut mapping = HashMap::new();
        let mut white = size;
        for b in blacklist {
            if b < size {
                while black.contains(&white) {
                    white += 1;
                }
                mapping.insert(b, white);
                white += 1;
            }
        }
        Self {
            size,
            mapping,
            seed: 0x1234_5678_9abc_def0,
        }
    }

    pub fn pick(&mut self) -> i32 {
        self.seed = self.seed.wrapping_mul(6364136223846793005).wrapping_add(1);
        let index = (self.seed % self.size as u64) as i32;
        *self.mapping.get(&index).unwrap_or(&index)
    }
}
