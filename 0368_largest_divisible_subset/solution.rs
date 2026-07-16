// LeetCode 0368 - Largest Divisible Subset
// https://leetcode.com/problems/largest-divisible-subset/

use std::collections::HashMap;

impl Solution {
    pub fn largest_divisible_subset(nums: Vec<i32>) -> Vec<i32> {
        let mut nums = nums;
        nums.sort_unstable();
        let mut chains: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut best: Vec<i32> = Vec::new();

        for num in nums {
            chains.insert(num, vec![num]);
            let keys: Vec<i32> = chains.keys().copied().collect();
            for prev in keys {
                if prev < num && num % prev == 0 {
                    let candidate_len = chains[&prev].len() + 1;
                    if candidate_len > chains[&num].len() {
                        let mut next = chains[&prev].clone();
                        next.push(num);
                        chains.insert(num, next);
                    }
                }
            }
            if chains[&num].len() > best.len() {
                best = chains[&num].clone();
            }
        }

        best
    }
}
