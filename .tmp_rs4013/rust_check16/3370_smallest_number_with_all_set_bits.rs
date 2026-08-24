struct Solution;
// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

impl Solution {
    pub fn smallest_number(n: i32) -> i32 {
        let mut x = 1;
        while x < n {
            x = x * 2 + 1;
        }
        x
    }
}

fn main() {}
