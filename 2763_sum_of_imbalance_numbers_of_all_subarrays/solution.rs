// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

use std::collections::{BTreeSet, HashSet};

impl Solution {
    pub fn sum_imbalance_numbers(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut seen = HashSet::new();
            let mut sorted_vals = BTreeSet::new();
            let mut imbalance = 0;
            for j in i..n {
                let x = nums[j];
                if seen.insert(x) {
                    if let Some(&nxt) = sorted_vals.range(x..).next() {
                        if nxt - x != 1 {
                            imbalance += 1;
                        }
                    }
                    if let Some(&prv) = sorted_vals.range(..x).next_back() {
                        if x - prv != 1 {
                            imbalance += 1;
                        }
                    }
                    if let (Some(&prv), Some(&nxt)) = (
                        sorted_vals.range(..x).next_back(),
                        sorted_vals.range(x..).next(),
                    ) {
                        if nxt - prv > 1 {
                            imbalance -= 1;
                        }
                    }
                    sorted_vals.insert(x);
                }
                ans += imbalance;
            }
        }
        ans
    }
}
