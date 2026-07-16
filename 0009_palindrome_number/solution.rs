// LeetCode 0009 - Palindrome Number
// https://leetcode.com/problems/palindrome-number/

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x != 0 && x % 10 == 0) {
            return false;
        }

        let mut value = x;
        let mut reversed_half = 0;
        while value > reversed_half {
            reversed_half = reversed_half * 10 + value % 10;
            value /= 10;
        }

        value == reversed_half || value == reversed_half / 10
    }
}
