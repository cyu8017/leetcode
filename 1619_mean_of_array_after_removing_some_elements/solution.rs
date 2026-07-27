// LeetCode 1619 - Mean of Array After Removing Some Elements
// https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

impl Solution {
    pub fn trim_mean(mut arr: Vec<i32>) -> f64 {
        arr.sort_unstable();
        let k = arr.len() / 20;
        let sum: i32 = arr[k..arr.len() - k].iter().sum();
        sum as f64 / (arr.len() - 2 * k) as f64
    }
}
