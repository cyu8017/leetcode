// LeetCode 2225 - Find Players With Zero or One Losses
// https://leetcode.com/problems/find-players-with-zero-or-one-losses/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut lose = HashMap::new();
        let mut seen = HashSet::new();
        for m in matches {
            seen.insert(m[0]);
            seen.insert(m[1]);
            *lose.entry(m[1]).or_insert(0) += 1;
        }
        let mut zero = Vec::new();
        let mut one = Vec::new();
        for p in seen {
            let l = *lose.get(&p).unwrap_or(&0);
            if l == 0 {
                zero.push(p);
            } else if l == 1 {
                one.push(p);
            }
        }
        zero.sort_unstable();
        one.sort_unstable();
        vec![zero, one]
    }
}
