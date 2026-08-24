// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

use std::collections::HashSet;

impl Solution {
    pub fn fair_candy_swap(alice_sizes: Vec<i32>, bob_sizes: Vec<i32>) -> Vec<i32> {
        let diff = (alice_sizes.iter().sum::<i32>() - bob_sizes.iter().sum::<i32>()) / 2;
        let bob: HashSet<i32> = bob_sizes.into_iter().collect();
        for a in alice_sizes {
            if bob.contains(&(a - diff)) {
                return vec![a, a - diff];
            }
        }
        vec![]
    }
}
