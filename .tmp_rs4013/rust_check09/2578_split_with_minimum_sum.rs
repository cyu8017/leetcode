struct Solution;

// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

impl Solution {
    pub fn split_num(mut num: i32) -> i32 {
        let mut digits = Vec::new();
        while num > 0 {
            digits.push(num % 10);
            num /= 10;
        }
        digits.sort_unstable();
        let mut a = 0;
        let mut b = 0;
        for (i, d) in digits.into_iter().enumerate() {
            if i % 2 == 0 {
                a = a * 10 + d;
            } else {
                b = b * 10 + d;
            }
        }
        a + b
    }
}

fn main() {}
