// LeetCode 1460 - Make Two Arrays Equal by Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn can_be_equal(target: Vec<i32>, arr: Vec<i32>) -> bool {
        let mut c = HashMap::new();
        for x in target {
            *c.entry(x).or_insert(0) += 1;
        }
        for x in arr {
            *c.entry(x).or_insert(0) -= 1;
        }
        c.values().all(|&v| v == 0)
    }
}
