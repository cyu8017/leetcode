// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

use std::collections::HashMap;

impl Solution {
    pub fn min_swaps_couples(mut row: Vec<i32>) -> i32 {
        let mut pos = HashMap::new();
        for (i, &person) in row.iter().enumerate() {
            pos.insert(person, i);
        }
        let mut swaps = 0;
        for i in (0..row.len()).step_by(2) {
            let partner = row[i] ^ 1;
            if row[i + 1] == partner {
                continue;
            }
            let j = pos[&partner];
            pos.insert(row[i + 1], j);
            row[j] = row[i + 1];
            row[i + 1] = partner;
            pos.insert(partner, i + 1);
            swaps += 1;
        }
        swaps
    }
}
