// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

impl Solution {
    pub fn sort_by(arr: Vec<i32>, f: impl Fn(i32) -> f64) -> Vec<i32> {
        let mut out = arr;
        out.sort_by(|a, b| f(*a).partial_cmp(&f(*b)).unwrap());
        out
    }
}
