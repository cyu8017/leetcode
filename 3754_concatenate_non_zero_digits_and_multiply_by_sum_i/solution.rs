// LeetCode 3754 - Concatenate Non Zero Digits And Multiply By Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

impl Solution {
    pub fn sum_and_multiply(mut n: i32) -> i64 {
        let mut p = 1i32;
        let mut x = 0i32;
        let mut s = 0i32;
        while n > 0 {
            let v = n % 10;
            if v != 0 {
                s += v;
                x += p * v;
                p *= 10;
            }
            n /= 10;
        }
        x as i64 * s as i64
    }
}
