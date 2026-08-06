// LeetCode 1346 - Check If N and Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

use std::collections::HashSet;

impl Solution {
    pub fn check_if_exist(arr: Vec<i32>) -> bool {
        let mut seen = HashSet::new();
        for value in arr {
            if seen.contains(&(value * 2)) || (value % 2 == 0 && seen.contains(&(value / 2))) {
                return true;
            }
            seen.insert(value);
        }
        false
    }
}
