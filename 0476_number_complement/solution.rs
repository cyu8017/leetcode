// LeetCode 0476 - Number Complement
// https://leetcode.com/problems/number-complement/

impl Solution {
    pub fn find_complement(num: i32) -> i32 {
        let mut mask = num;
        mask |= mask >> 1;
        mask |= mask >> 2;
        mask |= mask >> 4;
        mask |= mask >> 8;
        mask |= mask >> 16;
        num ^ mask
    }
}
