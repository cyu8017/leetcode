struct Solution;
// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

use std::collections::HashMap;

impl Solution {
    pub fn min_groups_for_valid_assignment(balls: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for b in &balls {
            *freq.entry(*b).or_insert(0) += 1;
        }
        let counts: Vec<i32> = freq.values().copied().collect();
        let min_f = *counts.iter().min().unwrap_or(&1);
        for size in (1..=min_f).rev() {
            let mut ok = true;
            let mut groups = 0;
            for &c in &counts {
                let rem = c % (size + 1);
                let g2 = c / (size + 1);
                if rem == 0 {
                    groups += g2;
                } else if size - rem <= g2 {
                    groups += g2 + 1;
                } else {
                    ok = false;
                    break;
                }
            }
            if ok {
                return groups;
            }
        }
        balls.len() as i32
    }
}

fn main() {}
