// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_rounds(tasks: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();
        for t in tasks {
            *freq.entry(t).or_insert(0) += 1;
        }
        let mut ans = 0;
        for &c in freq.values() {
            if c == 1 {
                return -1;
            }
            ans += (c + 2) / 3;
        }
        ans
    }
}
