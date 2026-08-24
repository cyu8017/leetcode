struct Solution;

// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

impl Solution {
    pub fn count_digits(num: i32) -> i32 {
        let mut ans = 0;
        let mut x = num;
        while x > 0 {
            let d = x % 10;
            if d != 0 && num % d == 0 {
                ans += 1;
            }
            x /= 10;
        }
        ans
    }
}

fn main() {}
