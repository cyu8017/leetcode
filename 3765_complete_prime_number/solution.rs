// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

impl Solution {
    fn is_prime(x: i32) -> bool {
        if x < 2 {
            return false;
        }
        let mut i = 2;
        while i * i <= x {
            if x % i == 0 {
                return false;
            }
            i += 1;
        }
        true
    }

    pub fn complete_prime(num: i32) -> bool {
        let s = num.to_string();
        let mut x = 0;
        for c in s.bytes() {
            x = x * 10 + (c - b'0') as i32;
            if !Self::is_prime(x) {
                return false;
            }
        }
        x = 0;
        let mut p = 1;
        for c in s.bytes().rev() {
            x = p * (c - b'0') as i32 + x;
            p *= 10;
            if !Self::is_prime(x) {
                return false;
            }
        }
        true
    }
}
