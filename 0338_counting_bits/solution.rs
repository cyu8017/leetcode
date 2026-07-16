// LeetCode 0338 - Counting Bits
// https://leetcode.com/problems/counting-bits/

impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let size = (n + 1) as usize;
        let mut result = vec![0; size];
        for index in 1..=n as usize {
            result[index] = result[index & (index - 1)] + 1;
        }
        result
    }
}
