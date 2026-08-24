struct Solution;
// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

impl Solution {
    pub fn maximum_value(n: i32, s: i32, m: i32) -> i64 {
        if n == 1 {
            return s as i64;
        }
        s as i64 + (n as i64 / 2) * (m as i64 - 1) + 1
    }
}

fn main() {}
