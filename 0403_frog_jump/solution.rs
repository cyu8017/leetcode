// LeetCode 0403 - Frog Jump
// https://leetcode.com/problems/frog-jump/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn can_cross(stones: Vec<i32>) -> bool {
        let stone_set: HashSet<i32> = stones.iter().copied().collect();
        let mut jumps: HashMap<i32, HashSet<i32>> =
            stones.iter().map(|&stone| (stone, HashSet::new())).collect();

        jumps.get_mut(&0).unwrap().insert(0);

        for &stone in &stones {
            let current_jumps: Vec<i32> = jumps.get(&stone).unwrap().iter().copied().collect();
            for jump in current_jumps {
                for next_jump in [jump - 1, jump, jump + 1] {
                    if next_jump <= 0 {
                        continue;
                    }
                    let next_stone = stone + next_jump;
                    if stone_set.contains(&next_stone) {
                        jumps.get_mut(&next_stone).unwrap().insert(next_jump);
                    }
                }
            }
        }

        !jumps.get(stones.last().unwrap()).unwrap().is_empty()
    }
}
