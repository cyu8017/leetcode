// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

use std::collections::HashMap;

impl Solution {
    pub fn best_hand(ranks: Vec<i32>, suits: Vec<char>) -> String {
        if suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4] {
            return "Flush".to_string();
        }
        let mut cnt = HashMap::new();
        let mut best = 0;
        for r in ranks {
            let e = cnt.entry(r).or_insert(0);
            *e += 1;
            best = best.max(*e);
        }
        if best >= 3 {
            "Three of a Kind".to_string()
        } else if best == 2 {
            "Pair".to_string()
        } else {
            "High Card".to_string()
        }
    }
}
