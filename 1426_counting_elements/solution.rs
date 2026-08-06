// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

use std::collections::HashSet;

impl Solution {
    pub fn count_elements(arr: Vec<i32>) -> i32 {
        let values: HashSet<i32> = arr.iter().copied().collect();
        arr.iter().filter(|&&v| values.contains(&(v + 1))).count() as i32
    }
}
