struct Solution;
// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

impl Solution {
    pub fn generate_key(mut num1: i32, mut num2: i32, mut num3: i32) -> i32 {
        let mut ans = 0;
        let mut mul = 1;
        for _ in 0..4 {
            let d = num1 % 10;
            let d = d.min(num2 % 10).min(num3 % 10);
            ans += d * mul;
            mul *= 10;
            num1 /= 10;
            num2 /= 10;
            num3 /= 10;
        }
        ans
    }
}

fn main() {}
