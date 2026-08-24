// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_card_pickup(cards: Vec<i32>) -> i32 {
        let mut last = HashMap::new();
        let mut ans = -1;
        for (i, &c) in cards.iter().enumerate() {
            if let Some(&prev) = last.get(&c) {
                let diff = i as i32 - prev + 1;
                if ans == -1 || diff < ans {
                    ans = diff;
                }
            }
            last.insert(c, i as i32);
        }
        ans
    }
}
