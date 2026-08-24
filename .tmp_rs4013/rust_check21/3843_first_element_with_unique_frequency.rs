struct Solution;
// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn first_unique_freq(nums: Vec<i32>) -> i32 {
        let mut cnt = HashMap::new();
        for &x in &nums {
            *cnt.entry(x).or_insert(0) += 1;
        }
        let mut freq = HashMap::new();
        for &v in cnt.values() {
            *freq.entry(v).or_insert(0) += 1;
        }
        for x in nums {
            if freq[&cnt[&x]] == 1 {
                return x;
            }
        }
        -1
    }
}
