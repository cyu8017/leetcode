// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

impl Solution {
    pub fn map(arr: Vec<i32>, f: impl Fn(i32, i32) -> i32) -> Vec<i32> {
        arr.into_iter()
            .enumerate()
            .map(|(i, x)| f(x, i as i32))
            .collect()
    }
}
