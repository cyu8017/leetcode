struct Solution;
// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let total = n * (n + 1) / 2;
        let mut sum = 0;
        for x in 1..=n {
            sum += x;
            if sum == total - sum + x {
                return x;
            }
        }
        -1
    }
}

fn main() {}
