// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        arr.iter()
            .enumerate()
            .map(|(i, &x)| x * (((i + 1) * (n - i) + 1) / 2) as i32)
            .sum()
    }
}
