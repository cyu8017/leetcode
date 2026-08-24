struct Solution;
// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

impl Solution {
    pub fn is_balanced(num: String) -> bool {
        let mut even = 0;
        let mut odd = 0;
        for (i, c) in num.bytes().enumerate() {
            if i % 2 == 0 {
                even += (c - b'0') as i32;
            } else {
                odd += (c - b'0') as i32;
            }
        }
        even == odd
    }
}

fn main() {}
