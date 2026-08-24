// LeetCode 3688 - Bitwise OR of Even Numbers in an Array
// https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

impl Solution {
    pub fn even_number_bitwise_o_rs(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        for x in nums {
            if x % 2 == 0 {
                ans |= x;
            }
        }
        ans
    }
}
