// LeetCode 0191 - Number of 1 Bits
// https://leetcode.com/problems/number-of-1-bits/

impl Solution {
    pub fn hamming_weight(mut n: u32) -> i32 {
        let mut count = 0;
        while n != 0 {
            n &= n - 1;
            count += 1;
        }
        count
    }
}
