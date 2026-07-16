// LeetCode 0371 - Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        let mut a = a;
        let mut b = b;
        let mask = 0xFFFF_FFFFu32;

        while b != 0 {
            let carry = ((a & b) << 1) & mask as i32;
            a = (a ^ b) & mask as i32;
            b = carry;
        }

        if a <= 0x7FFF_FFFF {
            a
        } else {
            !(a ^ mask as i32)
        }
    }
}
