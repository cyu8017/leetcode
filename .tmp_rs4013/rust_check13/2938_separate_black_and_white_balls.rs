#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

impl Solution {
    pub fn minimum_steps(s: String) -> i64 {
        let mut ans = 0i64;
        let mut zeros = 0i64;
        for &c in s.as_bytes().iter().rev() {
            if c == b'0' {
                zeros += 1;
            } else {
                ans += zeros;
            }
        }
        ans
    }
}
