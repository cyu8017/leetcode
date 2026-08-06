// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

use std::collections::HashMap;

impl Solution {
    pub fn is_possible_divide(nums: Vec<i32>, k: i32) -> bool {
        if nums.len() as i32 % k != 0 {
            return false;
        }
        let mut counts = HashMap::new();
        for x in nums {
            *counts.entry(x).or_insert(0) += 1;
        }
        let mut keys: Vec<i32> = counts.keys().copied().collect();
        keys.sort_unstable();
        for start in keys {
            let amount = *counts.get(&start).unwrap_or(&0);
            if amount == 0 {
                continue;
            }
            for value in start..start + k {
                let c = counts.entry(value).or_insert(0);
                if *c < amount {
                    return false;
                }
                *c -= amount;
            }
        }
        true
    }
}
