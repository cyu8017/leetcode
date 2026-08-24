// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

impl Solution {
    pub fn has_trailing_zeros(nums: Vec<i32>) -> bool {
        let mut even = 0;
        for v in nums {
            if v % 2 == 0 {
                even += 1;
                if even >= 2 {
                    return true;
                }
            }
        }
        false
    }
}
