struct Solution;
// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

impl Solution {
    pub fn smallest_number(n: i32, t: i32) -> i32 {
        let mut x = n;
        loop {
            let mut p = 1;
            let mut y = x;
            while y > 0 {
                p *= y % 10;
                y /= 10;
            }
            if p % t == 0 {
                return x;
            }
            x += 1;
        }
    }
}

fn main() {}
