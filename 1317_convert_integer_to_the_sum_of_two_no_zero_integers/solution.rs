// LeetCode 1317 - Convert Integer to the Sum of Two No-Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

impl Solution {
    pub fn get_no_zero_integers(n: i32) -> Vec<i32> {
        let valid = |v: i32| !v.to_string().contains('0');
        for first in 1..n {
            if valid(first) && valid(n - first) {
                return vec![first, n - first];
            }
        }
        vec![]
    }
}
