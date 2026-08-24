// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

impl Solution {
    pub fn max_number(n: i64) -> i64 {
        let len = 64 - (n as u64).leading_zeros();
        (1i64 << (len - 1)) - 1
    }
}
