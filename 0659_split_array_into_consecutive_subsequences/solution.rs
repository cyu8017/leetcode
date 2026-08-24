// LeetCode 0659 - Split Array into Consecutive Subsequences
// https://leetcode.com/problems/split-array-into-consecutive-subsequences/

use std::collections::HashMap;

impl Solution {
    pub fn is_possible(nums: Vec<i32>) -> bool {
        let mut freq = HashMap::new();
        let mut tails = HashMap::new();
        for &num in &nums {
            *freq.entry(num).or_insert(0) += 1;
        }
        for &num in &nums {
            if freq[&num] == 0 {
                continue;
            }
            *freq.get_mut(&num).unwrap() -= 1;
            if *tails.get(&(num - 1)).unwrap_or(&0) > 0 {
                *tails.get_mut(&(num - 1)).unwrap() -= 1;
                *tails.entry(num).or_insert(0) += 1;
            } else if *freq.get(&(num + 1)).unwrap_or(&0) > 0 && *freq.get(&(num + 2)).unwrap_or(&0) > 0 {
                *freq.get_mut(&(num + 1)).unwrap() -= 1;
                *freq.get_mut(&(num + 2)).unwrap() -= 1;
                *tails.entry(num + 2).or_insert(0) += 1;
            } else {
                return false;
            }
        }
        true
    }
}
