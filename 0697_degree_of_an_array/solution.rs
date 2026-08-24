// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn find_shortest_sub_array(nums: Vec<i32>) -> i32 {
        let mut first = HashMap::new();
        let mut last = HashMap::new();
        let mut count = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            first.entry(num).or_insert(i);
            last.insert(num, i);
            *count.entry(num).or_insert(0) += 1;
        }
        let degree = *count.values().max().unwrap_or(&0);
        let mut best = i32::MAX;
        for (&num, &freq) in &count {
            if freq == degree {
                best = best.min((last[&num] - first[&num] + 1) as i32);
            }
        }
        best
    }
}
