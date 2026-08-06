// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

use std::collections::HashSet;

impl Solution {
    pub fn max_non_overlapping(nums: Vec<i32>, target: i32) -> i32 {
        let mut seen = HashSet::new();
        seen.insert(0);
        let mut prefix = 0;
        let mut answer = 0;
        for value in nums {
            prefix += value;
            if seen.contains(&(prefix - target)) {
                answer += 1;
                prefix = 0;
                seen.clear();
                seen.insert(0);
            } else {
                seen.insert(prefix);
            }
        }
        answer
    }
}
