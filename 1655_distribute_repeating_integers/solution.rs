// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn can_distribute(nums: Vec<i32>, mut quantity: Vec<i32>) -> bool {
        let mut freq = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let cnt: Vec<i32> = freq.into_values().collect();
        quantity.sort_by(|a, b| b.cmp(a));
        let m = quantity.len();
        let mut sums = vec![0; 1 << m];
        for mask in 1usize..(1 << m) {
            let bit = mask & mask.wrapping_neg();
            let idx = bit.trailing_zeros() as usize;
            sums[mask] = sums[mask ^ bit] + quantity[idx];
        }
        let mut dp: HashSet<usize> = HashSet::from([0]);
        for c in cnt {
            let mut nxt = dp.clone();
            for &mask in &dp {
                let left = ((1usize << m) - 1) ^ mask;
                let mut sub = left;
                while sub > 0 {
                    if sums[sub] <= c {
                        nxt.insert(mask | sub);
                    }
                    sub = (sub - 1) & left;
                }
            }
            dp = nxt;
        }
        dp.contains(&((1usize << m) - 1))
    }
}
