// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

use std::collections::HashSet;

impl Solution {
    pub fn closest_to_target(arr: Vec<i32>, target: i32) -> i32 {
        let mut answer = i32::MAX;
        let mut current: HashSet<i32> = HashSet::new();
        for value in arr {
            let mut next = HashSet::new();
            next.insert(value);
            for &previous in &current {
                next.insert(value & previous);
            }
            current = next;
            for &candidate in &current {
                answer = answer.min((candidate - target).abs());
            }
        }
        answer
    }
}
