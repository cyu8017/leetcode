// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        if n == 0 {
            return 1;
        }
        let bits = 32 - n.leading_zeros();
        let mask = ((1i64 << bits) - 1) as i32;
        n ^ mask
    }
}
