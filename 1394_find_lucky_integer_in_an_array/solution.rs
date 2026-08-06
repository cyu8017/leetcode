// LeetCode 1394 - Find Lucky Integer in an Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn find_lucky(arr: Vec<i32>) -> i32 {
        let mut counts = HashMap::new();
        for x in arr {
            *counts.entry(x).or_insert(0) += 1;
        }
        counts
            .into_iter()
            .filter(|&(x, c)| x == c)
            .map(|(x, _)| x)
            .max()
            .unwrap_or(-1)
    }
}
