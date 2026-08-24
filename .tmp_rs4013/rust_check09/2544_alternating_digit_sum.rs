struct Solution;

// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/

impl Solution {
    pub fn alternate_digit_sum(mut n: i32) -> i32 {
        let mut s = Vec::new();
        while n > 0 {
            s.push(n % 10);
            n /= 10;
        }
        let mut ans = 0;
        let mut sign = 1;
        for i in (0..s.len()).rev() {
            ans += sign * s[i];
            sign = -sign;
        }
        ans
    }
}

fn main() {}
