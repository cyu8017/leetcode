// LeetCode 2505 - Bitwise OR of All Subsequence Sums
// https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

impl Solution {
    pub fn subsequence_sum_or(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut prefix = 0i64;
        for x in nums {
            prefix += x as i64;
            ans |= x as i64 | prefix;
        }
        ans
    }
}
