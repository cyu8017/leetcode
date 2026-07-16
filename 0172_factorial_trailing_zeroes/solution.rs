// LeetCode 0172 - Factorial Trailing Zeroes
// https://leetcode.com/problems/factorial-trailing-zeroes/

impl Solution {
    pub fn trailing_zeroes(mut n: i32) -> i32 {
        let mut count = 0;
        while n > 0 {
            n /= 5;
            count += n;
        }
        count
    }
}