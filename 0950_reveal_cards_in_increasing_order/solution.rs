// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

use std::collections::VecDeque;

impl Solution {
    pub fn deck_revealed_increasing(mut deck: Vec<i32>) -> Vec<i32> {
        deck.sort_unstable();
        let n = deck.len();
        let mut idx: VecDeque<usize> = (0..n).collect();
        let mut ans = vec![0; n];
        for card in deck {
            let i = idx.pop_front().unwrap();
            ans[i] = card;
            if let Some(front) = idx.pop_front() {
                idx.push_back(front);
            }
        }
        ans
    }
}
