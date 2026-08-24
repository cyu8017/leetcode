struct Solution;
fn main() {}

// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

impl Solution {
    pub fn deep_filter<F: Fn(i32) -> bool>(obj: Vec<i32>, fn_: F) -> Vec<i32> {
        obj.into_iter().filter(|&v| fn_(v)).collect()
    }
}
