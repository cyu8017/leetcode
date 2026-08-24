struct Solution;
// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

use std::collections::HashSet;

impl Solution {
    pub fn max_sum(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        let mut sum = 0;
        let mut has_pos = false;
        let mut max_neg = -1_000_000_000;
        for x in nums {
            if x < 0 {
                if x > max_neg {
                    max_neg = x;
                }
                continue;
            }
            has_pos = true;
            if seen.insert(x) {
                sum += x;
            }
        }
        if has_pos {
            sum
        } else {
            max_neg
        }
    }
}

fn main() {}
