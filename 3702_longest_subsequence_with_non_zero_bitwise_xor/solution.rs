// LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
// https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        let mut xorv = 0;
        let mut cnt0 = 0;
        for &x in &nums {
            xorv ^= x;
            if x == 0 {
                cnt0 += 1;
            }
        }
        let n = nums.len() as i32;
        if xorv != 0 {
            n
        } else if cnt0 == n {
            0
        } else {
            n - 1
        }
    }
}
