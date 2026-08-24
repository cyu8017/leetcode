struct Solution;
// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

impl Solution {
    pub fn largest_integer(n: i32, mut s: i32) -> i32 {
        if n * 9 < s {
            return -1;
        }
        let mut ans = 0;
        for _ in 0..n {
            let x = if s < 9 { s } else { 9 };
            ans = ans * 10 + x;
            s -= x;
        }
        ans
    }
}

fn main() {}
