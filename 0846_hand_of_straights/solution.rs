// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

use std::collections::BTreeMap;

impl Solution {
    pub fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
        if hand.len() as i32 % group_size != 0 {
            return false;
        }
        let mut count = BTreeMap::new();
        for x in hand {
            *count.entry(x).or_insert(0) += 1;
        }
        let keys: Vec<i32> = count.keys().copied().collect();
        for start in keys {
            while *count.get(&start).unwrap_or(&0) > 0 {
                for x in start..start + group_size {
                    let entry = count.entry(x).or_insert(0);
                    if *entry == 0 {
                        return false;
                    }
                    *entry -= 1;
                }
            }
        }
        true
    }
}
